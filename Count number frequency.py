value1 = "08989082882348823838"

dict = {}
for x in value1:
    if x not in dict:
        dict[x] = 0
    else:
        dict[x] += 1

max = 0
str = ""
for x in dict:
    if dict[x] > max:
        max = dict[x]
        str = x

print(str) 
