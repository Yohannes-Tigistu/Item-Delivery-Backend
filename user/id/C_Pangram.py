n = int(input())
s = input()
arr = list(s)

for c in range(len(s)):
    arr[c] = s[c].lower()

mySet = set(arr)
if len(mySet) < 26:
    print("NO")
else:
    print("YES")