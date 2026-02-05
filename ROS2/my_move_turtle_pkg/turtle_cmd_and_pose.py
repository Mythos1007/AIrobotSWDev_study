import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from my_first_package_msgs.msg import CmdAndPoseVel
#from my_move_turtle_pkg.move_turtle_pub import Twist
from geometry_msgs.msg import Twist
class CmdAndPose(Node):

    def __init__(self):
        super().__init__('turtle_cmd_pose')
        self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
        self.cmd_pose = CmdAndPoseVel()
        #self.twist_pose = Twist()
        self.twist_pose = self.create_subscription(Twist, 'turtle1/cmd_vel', self.callback_cmd_vel, 10)

    def callback_pose(self, msg):
       self.cmd_pose.pose_x = msg.x
       self.cmd_pose.pose_y = msg.y
       self.cmd_pose.linear_vel = msg.linear_velocity
       self.cmd_pose.angular_vel = msg.angular_velocity

       print(self.cmd_pose)

    def callback_cmd_vel(self, msg):
       self.cmd_pose.cmd_vel_linear = msg.linear.x
       self.cmd_pose.cmd_vel_angular = msg.angular.z
       print(self.cmd_pose)


def main(args=None):
    rclpy.init(args=args)
    node = CmdAndPose()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()
