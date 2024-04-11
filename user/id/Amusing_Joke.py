guest = input()
host = input()
conc = input()
guest1 = list(guest)
host1 = list(host)
conc1 = list(conc)
count1 = 0
count2 = 0
if len(conc) != (len(guest) + len(host)):
    print("NO") 
else:
    for c in conc1:
        if c in guest1:
            guest1.pop(guest1.index(c))
            conc1.pop(conc1.index(c))
            count1 += 1
    for c in conc1:
        if c in host1:
            host1.pop(host1.index(c))
            count2 += 1
    if count1 + count2 == len(conc):
        print("YES")
    else:
        print("NO")
        


