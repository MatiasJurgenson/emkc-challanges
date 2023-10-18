value1 = "3,9,10,-5,2,-7,9,2"
#output 10,9,9,7,5,3,2,2

value1 = value1.split(",")

for i in range(len(value1)):
    max_id = i
    for x in range(i, len(value1)):
        if int(value1[x]) > int(value1[max_id]):
            max_id = x

    temp = value1[i]        
    value1[i] = value1[max_id]
    value1[max_id] = temp

print((",").join(value1))