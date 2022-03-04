##리스트 컴프리헨션
a=[i for i in range(10)]
print(a)

##리스트 인덱싱
print(a[7])
print(a[-1])
a[3] = 7
print(a)

##리스트 슬라이싱
print(a[1:4])

##리스트 관련 메서드
b=[1,4,3]

b.append(2)

print(b)

b.sort()
print(b)

b.sort(reverse = True)
print(b)

b.reverse()
print(b)

b.insert(2, 3)
print(b)

print(b.count(3))

b.remove(1)
print(b)
