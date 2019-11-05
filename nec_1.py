start = input()
end = input()

arr = [41,42,43,44,45,46,47,48,49, '4A','4B','4C','4D','4E','4F',50,51,52,53,54,55,56,57,58,59,'5A']

num1 = ord(start) - ord('A')
num2 = ord(end) - ord('A')

for i in range(num1, num2+1):
    print (arr[i])
