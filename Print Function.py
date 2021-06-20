if __name__ == '__main__':
    n = int(input())

a = []
s = ''
for i in range(1, n+1):
    a.append(i)

for j in a:
    s+=str(j)
print(s)