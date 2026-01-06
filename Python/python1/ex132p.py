str1_input = input("문자열 입력> ")
str2_input = input("문자열 입력> ")

print()
print(str1_input, str2_input)

tem = str1_input
str1_input = str2_input
str2_input = tem

print(str1_input, str2_input)