s1=list('abcdefghifghi')
s2=list('fghijklmnfghi')
s3=[]
count=0
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if(s1[i]==s2[j]):
            s3.append(s1[i])
            s1[j]='A'
            count+=1
print(count)
print(''.join(s3))
