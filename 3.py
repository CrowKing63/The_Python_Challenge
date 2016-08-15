f = open("equality.txt", 'r')
data = f.read()
f.close()

result = ""

for i in range(3, len(data)):
    if data[i].islower():
        if data[i-4:i].isalpha() and data[i+1:i+5].isalpha():
            if data[i-3:i].isupper() and data[i+1:i+4].isupper():
                if data[i-4].islower() and data[i+4].islower():
                       result += data[i]

print result
