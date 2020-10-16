lst = [10, 20, 'pratyush', "agnihotri", 30.30]
print(lst)

print(lst[2])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append(49)
print(lst)

lst.remove("pratyush")
del(lst[1])
print(lst)

print(max(lst))
print(min(lst))
lst.insert(3,99)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.clear()
print(lst)