XL = int(input())
XI = int(input())
y = float(input())
X = XL + XI

if X >= 10:
    X = 1
else:
    X = 0

if XI < 1:
    X = 0

if y >= 3.5:
    y = 1    
else:
    y = 0
    
p = (15000 + 4000*XI)*X*y

if p > 150000:
    p = 150000

print(p)
