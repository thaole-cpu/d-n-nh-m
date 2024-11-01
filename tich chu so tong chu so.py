def check(a):
    s =0
    m=1
    for i in range(len(a)):
        if i % 2 == 1:
            s += int( a[i])
    for i in range(0,len(a),2):
              if int(a[i]) !=0:
                    m *=int(a[i])
    return (str(m)  +" " +str(s))
for t in range(int(input())):
    print(check(input()))