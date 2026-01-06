def test(function):
    def wrapper():
        print("인사 시작")
        function()
        print("인사 종료")
    return wrapper

@test
def hello():
    print('hello')

hello()