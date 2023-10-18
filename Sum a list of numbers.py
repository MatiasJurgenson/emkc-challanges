value1 = "3,9,10,5,2,7,9,2"
#output 47

str_list = value1.split(",")
output = 0
for x in str_list:
    output += int(x)

print(output)