"""
百分制成绩转等级制
90分以上 A
80分 ~ 89分 B
70分 ~ 79分 C
60分 ~ 69分 D
60分以下 E


Author: liwb
Version: 0.0.1
"""

score = float(input('请输入分数 '))

if score > 99:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('对应等级', grade)
