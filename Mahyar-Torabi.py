def topic(y,dars):
    for i in range(1,len(y)):
        dars.append(y[i])
        if(i==len(y)-1 or len(y)==1):
            print(y[i],end = ' ')
        else:
            print(y[i],end = ', ')
    print('Added!')
def score(y,asli,l):
    for i in range(2,len(y),+2):
        asli[l][y[i]] = eval(y[i+1])
def ashar(y,x):
    while y%1!=0:
        y *=10
        x+=1
    return x
def report(y,asli,x,dars,ave):
    for i in range(len(dars)):
        print('-',dars[i],end = ': ')
        z = asli[x][dars[i]]
        y = ashar(z,0)
        y = 2-y
        if(y==2):
            y=1
        print(z,end = '0'*y)
        print()
        ave+=z
    print('=======')
    ave = int((ave/len(dars))*100)
    ave  = ave/100
    y = ashar(ave,0)
    y = 2-y
    print('ave',ave,end = '0'*y)
    print()
def mian(asli,x,dars,ave):
    for i in range(len(dars)):
        ave+= asli[x][dars[i]]
    return ave
def index_by_ave(asli,asami,ave,dars,x,tartib):
    for i in range(len(asami)):
        ave = mian(asli,i,dars,0)
        ave/=len(dars)
        tartib[ave] =  asami[i]
        x.append(ave)
    x.sort()
    for j in range(len(x)-1,-1,-1):
        print(tartib[x[j]])
def index_by(asami,asli,x,tartib,y):
    for i in range(len(asami)):
        z = asli[i][y]
        tartib[z] = asami[i]
        x.append(z)
    x.sort()
    for j in range(len(x)-1,-1,-1):
        print(tartib[x[j]])
def halat_1(y1,y2,asl,s,x):
    for i in range(len(y2)):
        if(y2[i] in y1):
            z = y2.index(y2[i])-y1.index(y2[i])
            if(y1.index(y2[i]) not in x):
                x.append(y1.index(y2[i]))
            if(z==0 or z==1):
                s+=1
    if(s>=len(y1) and len(x)>=4):
        nam[1]=asl
        daraje.append(1)
def halat_2(y,x,nam,daraje,count,s,mm):
    for i in range(len(y)):
        if(x[i] in y):
            if(x.index(x[i])==y.index(y[i])):
                s+=1
    if(s==len(x)-1):
        nam[1.5] = x
        count[mm] = 1
        daraje.append(1.5)
def halat_3(y,x,nam,daraje,s):
    for i in range(len(y)):
        if(x[i] in y):
            s+=1
    if(s==len(x)):
        ma = 0
        for j in range(len(x)):
            s1 = x.index(x[j])
            s2 = y.index(x[j])
            n = s1-s2
            if(n<0):
                n*=-1
            ma+=n
        nam[ma]=x
        daraje.append(ma)
dars = []
asami = []
asli = []
a = [0]
dastoor=['exit','topic','score','report','index_by_ave','index_by']
while a[0]!='exit':
    a = list(input().split())
    if(a[0]=='exit'):
        break
    elif(a[0]=='topic'):
        topic(a,dars)
    elif(a[0]=='score'):
        if(a[1] in asami):
            print('Some similar records founded, Do you update previous information?(y/n)')
            x = input()
            if(x=='y'):
                score(a,asli,asami.index(a[1]))
                print('Information Updated')
            elif(x=='n'):
                print('Request was ignored!')
            else:
                print('You entered uninterpretable command, Request was ignored!')
        else:
            asami.append(a[1])
            asli.append({})
            score(a,asli,len(asami)-1)
            print(a[1],'Scores Added!')
    elif(a[0]=='report'):
        print(a[1],'Scores:')
        print('-')
        x = asami.index(a[1])
        report(a,asli,x,dars,0)
    elif(a[0]=='index_by_ave'):
        index_by_ave(asli,asami,0,dars,[],{})
    elif(a[0]=='index_by'):
        index_by(asami,asli,[],{},a[1])
    else:
        count = [0]*len(dastoor)
        x = len(a[0])
        nam = {}
        daraje = []
        for i in range(len(dastoor)):
            q = len(dastoor[i])
            if(q==x):
                halat_2(a[0],dastoor[i],nam,daraje,count,0,i)
                if(count[i]==0):
                    halat_3(a[0],dastoor[i],nam,daraje,0)
            elif(q+1==x or q-1==x):
                if(q>x):
                    y1 = a[0]
                    y2 = dastoor[i]
                else:
                    y2 = a[0]
                    y1 = dastoor[i]
                halat_1(y1,y2,dastoor[i],0,[])
        if(len(daraje)!=0):
            daraje.sort()
            print('You entered uninterpretable command, Did you mean:')
            for i in range(len(daraje)):
                print('-',nam[daraje[i]])
        else:
            print('You entered uninterpretable command, Request was ignored!')

            





            
