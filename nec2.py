def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

string  = input()
sub = input()

cn = occurrences(string,sub)

print(cn)