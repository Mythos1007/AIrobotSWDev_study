import random

first_names = list("김이박최정강조윤장임한오서신권황안송류전홍고문양손배백허유남심노하곽성차주우구신임")
second_names = list("가강건경고관광교구규근기길나남노누단대도동두라래로루리마만명모무문미민바박백범별보봉부비빈사산서석선설성세소손솔수순숭슬승시신아안애양어연영예오옥완요용우원유윤율은의이익인일자잔장재전정제조주준중지진찬창채천철초춘충치태판하한해허현형혜호홍화환황회휘효훈희")
with open('students.txt', 'w') as file:
    for i in range(30):
        id = i
        name = (random.choice(first_names) + random.choice(second_names) + random.choice(second_names))
        math = random.randint(0, 100)
        english = random.randint(0, 100)
        file.write('{},{},{},{}\n'.format(id, name, math, english))
