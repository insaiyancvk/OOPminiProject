#Notation used for returning values of every function: [<encrypted string>,<function serial number>,<additional values(if any exist)>]

import random, string

caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1','2','3','4','5','6','7','8','9']

def enc_fun1(plain_text):
    pt = plain_text
    nstr=''
    n=0
    if pt[2].isupper():
        n=ord(pt[2])%64
    elif pt[2].islower():
        n=ord(pt[2])%96
    elif ord(pt[2])>47 and ord(pt[2])<58:
        n=ord(pt[2])%47
    else:
        n=1
    t = plain_text[::-1]
    for i in range(len(t)):
        if t[i].isupper():
            if (ord(t[i])%64)+n >= len(caps):
                nstr+=caps[(ord(t[i])%64)+n-len(caps)-1]
            else:
                nstr+=caps[(ord(t[i])%64)+n-1]
        elif t[i].islower():
            if (ord(t[i])%96)+n >= len(small):
                nstr+=small[(ord(t[i])%96)+n-len(small)-1]
            else:
                nstr+=small[(ord(t[i])%96)+n-1]
        elif ord(t[i])>47 and ord(t[i])<58:
            if (ord(t[i])%47)+n >= len(num):
                nstr+=num[(ord(t[i])%47)+n-len(num)-1]
            else:
                nstr+=num[(ord(t[i])%47)+n-1]
        else:
            nstr+= t[i]
    return [nstr,1,n]

def enc_fun2(plain_text):
    nstr=''
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(len(plain_text)))
    for i in range(0,2*len(plain_text)):
        if i%2==0:
            if i>=len(plain_text):
                nstr+= plain_text[int(i/2)-len(plain_text)]
            else:
                nstr+= plain_text[int(i/2)]
        else:
            if i>=len(x):
               nstr+= x[int(i/2)-len(plain_text)]
            else:
                nstr+= x[int(i/2)]
    return [nstr,2]

def enc_fun3(plain_text):
    grp=[]
    n=(len(plain_text))%5
    for i in range(0,int((len(plain_text))/5)):
        grp.append(plain_text[i*5:(i+1)*5])
        if i==int((len(plain_text)-1)/5)-1:
            grp.append(plain_text[(i+1)*5:((i+1)*5)+n])

    grpstr = ''.join(grp[::-1])
    nstr=''
    for i in range(len(grpstr)):
        if grpstr[i].isupper():
            if (ord(grpstr[i])%64)+5 >= len(caps):
                nstr+=caps[(ord(grpstr[i])%64)+5-len(caps)-1]
            else:
                nstr+=caps[(ord(grpstr[i])%64)+5-1]
        elif grpstr[i].islower():
            if (ord(grpstr[i])%96)+5 >= len(small):
                nstr+=small[(ord(grpstr[i])%96)+5-len(small)-1]
            else:
                nstr+=small[(ord(grpstr[i])%96)+5-1]
        elif ord(grpstr[i])>47 and ord(grpstr[i])<58:
            if (ord(grpstr[i])%47)+5 >= len(num):
                nstr+=num[(ord(grpstr[i])%47)+5-len(num)-1]
            else:
                nstr+=num[(ord(grpstr[i])%47)+5-1]
        elif ord(grpstr[i])>122:
            nstr+=chr(ord(grpstr[i]))
        else:
            nstr+=chr(ord(grpstr[i]))
    return [nstr,3]

def enc_fun4(plain_text,dob):
    if str(dob).isdigit()==False:
        return -1 # returns -1 if the date of birth has text or special characters
    else:
        ndob = [int(x) for x in str(dob)]
        pt=plain_text
        nstr=''
        j=0
        # o=[]
        for i in range(len(pt)):
            if pt[i].isupper():
                if (ord(pt[i])%64)+ndob[j] >= len(caps):
                    nstr+=caps[(ord(pt[i])%64)+ndob[j]-len(caps)-1]
                else:
                    nstr+=caps[(ord(pt[i])%64)+ndob[j]-1]
            elif pt[i].islower():
                if (ord(pt[i])%96)+ndob[j] >= len(small):
                    nstr+=small[(ord(pt[i])%96)+ndob[j]-len(small)-1]
                else:
                    nstr+=small[(ord(pt[i])%96)+ndob[j]-1]
            elif ord(pt[i])>47 and ord(pt[i])<58:
                if (ord(pt[i])%47)+ndob[j] >= len(num):
                    nstr+=num[(ord(pt[i])%47)+ndob[j]-len(num)-1]
                else:
                    nstr+=num[(ord(pt[i])%47)+ndob[j]-1]
            else:
                nstr+= pt[i]
            j+=1
            if j==len(ndob):
                j=0
        return [''.join(str(i) for i in nstr),4]

def enc_fun5(plain_text,n):
    generated_strings=[]
    nstr= ''
    pt = plain_text
    nn=0
    for i in range(n):
        generated_strings.append(''.join(random.choice(string.ascii_lowercase) for _ in range(len(plain_text))))
    for j in range(len(generated_strings)):
        for i in range(len(plain_text)):
            if pt[i].islower():
                nn= ord(generated_strings[j][i])%96
                if ord(pt[i])+nn>=123:
                    nstr+= chr((ord(pt[i]))+nn-122+97)
                else:
                    nstr+= chr(ord(pt[i])+nn)
            elif pt[i].isupper():
                nn= ord(generated_strings[j][i])%96
                if ord(pt[i])+nn>=90:
                    nstr+= chr((ord(pt[i]))+nn-90+65)
                else:
                    nstr+= chr(ord(pt[i])+nn)
            else:
                nstr+= pt[i]
        pt = nstr
    return [pt[-len(plain_text):],5,generated_strings]

def enc_fun6(plain_text):
    a=plain_text
    r=(a[::-1])
    nstr=[]
    for i in range(len(r)):
        if ord(r[i])>=97 and ord(r[i])<=126:
            nstr.append(chr(ord(r[i])-64))
        else:
            nstr.append(r[i])
    return [''.join(str(i) for i in nstr),6]

def selector(cypher_text,i,d):
    enc_funs={
                "2":enc_fun2(cypher_text),
                "3":enc_fun3(cypher_text),
                "4":enc_fun4(cypher_text,int(d))
            } 
    return enc_funs[i][0]

def encryptor(text, key):
    text=str(text)
    cypher_text=text[:]
    if str(key).isdigit():
        for i in ["4","2"]:
            cypher_text=selector(cypher_text,i,d=key)
        return cypher_text
    else:
        return -1 # returns -1 if the key has any non-numeric character

# print(enc_fun5("a",1))