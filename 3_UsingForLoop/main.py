foods = ['Potato', 'Tomato', 'Ginger', 'Garlic', 'Coriander']

for f in foods:
    print(f)
    print(len(f))

print('Limiting the number of values to be printed')
for f in foods[:2]:
    print(f)
    print(len(f))