import re
senha = input()
if bool(re.search('^[a-z]*$',senha)) and bool(re.search('^[A-Z]*$',senha)) and bool(re.search('^[0-9]*$',senha)) and 6 <= len(senha) <= 15:
    i = 0
    flag = True
    while i < len(senha)-2 and flag:
        if ord(senha[i]) + 1 == ord(senha[i+1]):
            print("False")
            flag = False
        else:
            print("True")
            flag = False
        i += 1
else:
    print("Falseasdsda")
