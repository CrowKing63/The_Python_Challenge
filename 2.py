f = open("C:\Users\uitaek\Documents\The Python Challenge\The Python Challenge 2.txt", 'r')
data = f.read()
f.close()
checker = ['%', '$', '@', '_', '^', '#', ')', '&', '!', '+', ']', '*', '}', '[', '(', '{', '\n']
result = ""

for i in data:
    if i in checker:
        pass
    else:
        result += i

print result
