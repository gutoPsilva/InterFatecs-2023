string = input()
print(string)
reverseds = ""
stringr = [*string]
stringr.reverse()
for char in stringr:
    reverseds += char
print(reverseds)
