import datetime

string1="this is {} {}"
A="A"
B="B"
print(string1.format(A,B))
count=0

while input("enter 1"):
    formatter="Ack by {} @{} SESA{}"
    time=datetime.datetime.now()
    date_time=time.strftime("%H:%M:%S")
    if count==0:
        OE="Max"
        SESA="242524"
        count=1
    else:
        OE="Brian"
        SESA="123445"
        count=0
    print(formatter.format(OE,date_time,SESA))

print('end of code')

formatter2=f"todays date is{date_time}"
print(formatter2)
