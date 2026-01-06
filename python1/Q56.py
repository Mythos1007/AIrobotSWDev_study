# cal = input("연산자 : ")
# a = int(input("a = "))
# b = int(input("b = "))

# if cal == "+":
#     print("결과 : ", a + b)
# elif cal == "-":
#     print("결과 : ", a - b)
# elif cal == "*":
#     print("결과 : ", a * b)
# elif cal == "/":
#     print("결과 : ", a / b)
# else:
#     print("오류")

a = int(input())
if a % 3 == 0:
    print("OK")
else:
    if a % 5 == 0:
        print("OK")
    else:
        print("NO")