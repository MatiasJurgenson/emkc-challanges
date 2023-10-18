value1 = "run,barn,yellow,Barracuda,shark,fish,swim"

words = value1.split(",")

longest = ""
longero = []

for word in words:
    word = word.strip()
    if len(word) == len(longest):
        longero.append(word)
    if len(word) > len(longest):
        longest = word.lower()
        longero = []
        longero.append(longest)

print(",".join(longero))