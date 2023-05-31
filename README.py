
diamond = int(input('별 최대 개수 : '))

if diamond % 2 == 1:
    i = 1
else :
    i = 2

for i in range(i, diamond+1, 2):
    blank = ' '*((diamond-i)//2)
    star = '*'*i 
    
    print(blank, star,blank)

for i in range(i-2, 0, -2):
    blank = ' '*((diamond-i)//2)
    star = '*'*i
    
    print(blank, star,blank)
    
# while문 사용
diamond = int(input('별 최대 개수 : '))

if diamond % 2 == 1:
    i = 1
else :
    i = 2


while i < diamond:
    blank = ' '*((diamond-i)//2)
    star = '*'*i
    print(blank, star)

    i += 2
    
