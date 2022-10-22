# 첫수를 넣으세요 2
a = input("첫 수를 넣으세요")
# 끝수를 넣으세요 4
b = input("끝 수를 넣으세요")
# 2에서 4까지의 합은 9입니다
aa = int(a)
bb = int(b)

sum = 0
for i in range(aa,bb+1):
    sum += i

#print(a , "부터", b ,"까지의 합은", sum, "입니다.")
print("{}에서 {}까지의 합은 {}입니다.".format(aa,bb,sum))