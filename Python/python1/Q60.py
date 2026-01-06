#filter(fuction, list), map(lamda, list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n1 = filter(lambda x:x%2==0, numbers)
n2 = map(lambda x:x*2, n1)

print(list(n2))

####

words = ["python", "map", "filter", "lambda", "hi", "education", "code"]

w1 =filter(lambda x: len(x)>5, words)
w2 = map(lambda x:len(x), w1)
print(list(w2))

####

scores = [35, 78, 92, 55, 61, 47, 88, 73]
s1 =filter(lambda x:x>=60, scores)
s2 = map(lambda x:x+5, s1)
print(list(s2))


