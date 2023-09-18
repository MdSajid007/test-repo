num=input("Enter the seconds:")
num=int(num)
hour=num/3600
minute=((num%3600)/60)
print(int(minute))
second=num%60
second=int(second)
print(num,"seconds=",int(hour),"hours",int(minute),"minutes",second,"seconds")