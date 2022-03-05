a = dict()
a['홍길동'] = 97
a['이순신'] = 98
a['최성근'] = 99

print(a)

b = {
    '최성근':100,
    '강나경':101
}

print(b)
print(b['최성근'])

key_list = list(b.keys())
print(key_list)

val_list = list(b.values())
print(val_list)
