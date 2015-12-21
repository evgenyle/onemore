"""
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
n = int(input())
m= n*n
a=[x+1 for x in range(m)]
c=[]
for x in range(0,m,n):
    c.append(a[x:x+n])
for i in range(len(c)):
    if i%2!=0:
        c[i]=c[i][::-1]
for i in range(len(c)):
    for x in range(len(c[i])):
        print (c[i][x],end=' ')
    print ()
