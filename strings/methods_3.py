#join
list = ['Holle', 'world']
print(' '.join(list))
print(' - '.join(list))
print('_'.join(list))

print("-" * 17)

#split
test = "Hello world"
print(test.split(' '))
test = "MyABC nameABC isABCSalim"
print(test.split('ABC'))

txt = '''Hello
How are you
Thanks i am fine'''
print(txt.split('\n'))
print(txt.splitlines())

txt = 'Hello\nHow are you\nThanks i am fine'
print(txt.split('\n'))
print(txt.splitlines())