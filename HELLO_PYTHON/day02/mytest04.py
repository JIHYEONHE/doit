# 홀/짝을 입력하시오 홀 or 짝
# 나 : 홀
# 컴 : 홀
# 결과 : 승리
from random import random
print("홀/짝을 입력하시오 홀 or 짝")
me = input("나:")
computer = ""
rnd = random()
#print(rnd)

if rnd>0.5:
    computer = "짝"
else:
    computer = "홀"
    
print("컴퓨터:",computer)

if me==computer:
    print("승리")
else:
    print("패배")
    


