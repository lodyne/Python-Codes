n=10
sum=0
i=1
while i<=n:
    i+=1                       #i=i+1
    sum+=i                  #sum=sum+i
    if i==6:
        continue
    elif i==8:
        break
    else:
         pass
    print(sum)
