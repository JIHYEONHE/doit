# 1에서 100까지의 정수중 3의 배수의 합을 구하시오

#a = list(range(101))
#b = 0
#for i in a:
#    if i%3==0:
#        b += i
#print(b)

# a = 0
# for i in range(1,101) :
#   i%3 == 0
#   a+=i
# print(a)

sum = 0
for i in range(1,101):
    if i % 3 == 0:
        sum += i
        print(i)
    
print("sum",sum)





