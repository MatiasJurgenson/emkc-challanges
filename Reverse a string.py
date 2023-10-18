value1 = "1010100100110110"
output = ""

lenght = len(value1)

for x in range(lenght):
     output += value1[lenght - 1 - x]
   
print(output)