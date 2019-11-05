str1 = input()
ls = []
if(str1[0] == '-'):
    ls.append(str1[0])
for i in range(len(str1)):
    if (str1[i].isdigit()):
        ls.append(str1[i])
print(''.join(ls))