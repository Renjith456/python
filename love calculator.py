name1="Kanye West"
name2="Kim Kardashian"
count1=0
count2=0
for i in name1:
    if i=='t' or i=='T' or i=='R' or i=='r'or  i=='u'or i=="U" or i=='E' or i=='e':
        count1+=1
    else:
        continue
for i in name2:
    if i=='t' or i=='T' or i=='R' or i=='r'or  i=='u'or i=="U" or i=='E' or i=='e':
        count1+=1
    else:
        continue
for j in name1:
    if j=='l' or j=='L' or j=='o' or j=='O'or  j=='v'or j=="V" or j=='E' or j=='e':
        count2+=1
    else:
        continue
for j in name2:
    if j=='l' or j=='L' or j=='o' or j=='O'or  j=='v'or j=="V" or j=='E' or j=='e':
        count2+=1
    else:
        continue

print(count1,count2)