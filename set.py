data = set([1,1,2,2,3,4,5])
print(data)

data2 = {3,3,4,5,5,6,7}
print(data2)

print(data | data2) #합집합

print(data & data2) #교집합

print(data - data2) #차집합

data.add(6) #추가
print(data)

data.update([7,8]) #여러개 추가
print(data)

data.remove(3) #제거
print(data)
