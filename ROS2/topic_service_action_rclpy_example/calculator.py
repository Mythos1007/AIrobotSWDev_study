import time

import rclpy
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from rclpy.action import ActionServer

from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSProfile, QoSReliabilityPolicy

from msg_srv_action_interface_example.msg import ArithmeticArgument
from msg_srv_action_interface_example.srv import ArithmeticOperator
from msg_srv_action_interface_example.action import ArithmeticChecker


class Calculator(Node):
    def __init__(self):
        super().__init__('calculator')

        # ✅ 아직 토픽 못 받았을 때 구분하려고 None으로 시작
        self.argument_a = None
        self.argument_b = None

        # ✅ 서비스에서 계산될 때마다 갱신될 값들
        self.argument_result = 0.0
        self.argument_formula = ''

        self.callback_group = ReentrantCallbackGroup()

        self.declare_parameter('qos_depth', 10)
        qos_depth = self.get_parameter('qos_depth').value

        qos = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=qos_depth,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        # ✅ Topic subscriber
        self.arithmetic_argument_subscriber = self.create_subscription(
            ArithmeticArgument,
            'arithmetic_argument',
            self.get_arithmetic_argument,
            qos,
            callback_group=self.callback_group
        )

        # ✅ Service server
        self.service = self.create_service(
            ArithmeticOperator,
            'arithmetic_operator',
            self.get_arithmetic_operator
        )

        # ✅ Action server
        self.arithmetic_action_server = ActionServer(
            self,
            ArithmeticChecker,
            'arithmetic_checker',
            self.execute_checker,
            callback_group=self.callback_group
        )
        self.calc_seq = 0
        self.last_seq_used = 0

        self.get_logger().info('Calculator node started (topic+service+action).')

    # ✅ subscription callback (이 함수가 "클래스 안"에 있어야 함)
    def get_arithmetic_argument(self, msg: ArithmeticArgument):
        self.argument_a = msg.argument_a
        self.argument_b = msg.argument_b
        self.get_logger().info(f'Subscribed a={self.argument_a}, b={self.argument_b}')

    # ✅ service callback
    def get_arithmetic_operator(self, request, response):
      if self.argument_a is None or self.argument_b is None:
        self.get_logger().warn('Arguments not received yet.')
        response.arithmetic_result = 0.0
        return response

      operator = request.arithmetic_operator
      result = self.calculate_given_formula(self.argument_a, self.argument_b, operator)

    # ✅ 저장 (액션이 이 값을 사용)
      self.argument_result = result

      op_str_map = {
        ArithmeticOperator.Request.PLUS: '+',
        ArithmeticOperator.Request.MINUS: '-',
        ArithmeticOperator.Request.MULTIPLY: '*',
        ArithmeticOperator.Request.DIVISION: '/',
    }
      op_str = op_str_map.get(operator, '?')
      self.argument_formula = f'{self.argument_a} {op_str} {self.argument_b} = {result}'

    # ✅ “새 계산 발생” 표시 (엔터칠 때마다 1 증가)
      self.calc_seq += 1

      response.arithmetic_result = result
      self.get_logger().info(f'Service calculated (seq={self.calc_seq}): {self.argument_formula}')
      return response


    def calculate_given_formula(self, a, b, operator):
        if operator == ArithmeticOperator.Request.PLUS:
            return a + b
        elif operator == ArithmeticOperator.Request.MINUS:
            return a - b
        elif operator == ArithmeticOperator.Request.MULTIPLY:
            return a * b
        elif operator == ArithmeticOperator.Request.DIVISION:
            if b == 0.0:
                self.get_logger().error('ZeroDivisionError!')
                return 0.0
            return a / b
        else:
            self.get_logger().error('Invalid operator.')
            return 0.0

    # ✅ action execute
    def execute_checker(self, goal_handle):
        self.get_logger().info('Execute arithmetic_checker action!')

        feedback_msg = ArithmeticChecker.Feedback()
        feedback_msg.formula = []

        total_sum = 0.0
        goal_sum = goal_handle.request.goal_sum
        last_status_time = time.time()

        while total_sum < goal_sum:
            # 엔터(서비스 호출)로 새 계산이 들어온 경우
            if self.calc_seq != self.last_seq_used:
                total_sum += self.argument_result
                feedback_msg.formula.append(self.argument_formula)
                self.last_seq_used = self.calc_seq

            # 상태 피드백은 계속 보냄 (0.5초마다)
            if time.time() - last_status_time >= 0.5:
                goal_handle.publish_feedback(feedback_msg)
                last_status_time = time.time()

            time.sleep(0.05)



        goal_handle.succeed()

        result = ArithmeticChecker.Result()
        result.all_formula = feedback_msg.formula
        result.total_sum = total_sum
        return result


def main(args=None):
    rclpy.init(args=args)
    node = Calculator()

    executor = MultiThreadedExecutor(num_threads=4)
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        executor.shutdown()
        node.arithmetic_action_server.destroy()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
