s = "1.23,2.4,3.123"
s = s.split(",")
total = 0
for i in s:
    total += float(i)
print(total)
