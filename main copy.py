# 1st program
print(9**0.5*5)

# 2st program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3st program
print(2*2+2, 2*(2+5), 2*2+2 == 2*(2+5), sep='\n')

# 4st program
s = '123.456'

# 1-й способ
print(int(s.split('.')[-1][0]))

# 2-й способ
for i, j in enumerate(s):
    if j =='.':
       print(s[i+1])
       break

# 3-й способ
print(int(float(s)*10)%10)

