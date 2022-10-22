#로또 생성하시오.
#import random
#num1 = random.randrange(1, 46)
#num2 = random.randrange(1, 46)
#num3 = random.randrange(1, 46)
#num4 = random.randrange(1, 46)
#num5 = random.randrange(1, 46)
#num6 = random.randrange(1, 46)

#print(num1,num2,num3,num4,num5,num6)

#for i in range(1,46):
#rnd = random()


from random import random

arr45 = [
    1,2,3,4,5       ,6,7,8,9,10,
    11,12,13,14,15  ,16,17,18,19,20,
    21,22,23,24,25  ,26,27,28,29,30,
    31,32,33,34,35  ,36,37,38,39,40,
    41,42,43,44,45
]

# arr45 = range(1,45+1)

for i in range(100):
    rnd = int(random()*len(arr45))
    a = arr45[0]
    b = arr45[rnd]
    arr45[0]=b
    arr45[rnd]=a

#배열 자르는 법
print(arr45[0:6])



        