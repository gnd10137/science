##import csv
##f=open("accident.csv", encoding="euc-kr")
##data=csv.reader(f)
##
##next(data)
##i,j=0,0
##days=[]
##days_sum=[0]*7
##
##for row in data :
##    row[2:]=map(int, row[2:])
##    days_sum[i%7]+=row[2]
##    i+=1
##    if j<7:
##        days.append(row[1])
##        j+=1
##mx=days_sum[0]
##mx_day=' '
##
##for i in range(1, len(days_sum)) :
##    if mx<days_sum[i] :
##        mx=days_sum[i]
##        mx_day=days[i]
##for i in range(7):
##    print(days[i], ':',days_sum[i])
##print("교통사고가 가장 많이 나는 날은 " +mx_day +"요일입니다.")

##import matplotlib.pyplot as plt
##x=["instargram","Tiktok","Facebook", "X"]
##y=[11569,89,30,54]
##plt.bar(x,y)
##plt.xticks(rotation=40)
##plt.show()

##import csv
##f=open("accident.csv", encoding="euc-kr")
##data=csv.reader(f)
##
##next(data)
##i,j=0,0
##days=[]
##days_sum=[0]*7
##
##for row in data :
##    row[2:]=map(int, row[2:])
##    days_sum[i%7]+=row[2]
##    i+=1
##    if j<7:
##        days.append(row[1])
##        j+=1
##
##import matplotlib.pyplot as plt
##plt.rc("font", family = "Malgun Gothic")
##plt.title("요일별 교통사고 건수")
##plt.bar(days,days_sum)
##plt.show()

##import matplotlib.pyplot as plt
##
##number=[27000000,4000,130000,5700000]
##label=["lol", "brawl", "valorant", "roblox"]
##color=["mistyrose", "lightgreen", "salmon", "lightskyblue"]
##
##plt.title("Favorite game")
##plt.axis("equal")
##plt.pie(number, labels=label, autopct="%.1f%%", colors=color,explode=
##(0.2,0,0,0))
##plt.legend()
##plt.show()

import csv
f=open("accident.csv", encoding="euc-kr")
data=csv.reader(f)

next(data)
i,j=0,0
days=[]
days_sum=[0]*7

for row in data :
    row[2:]=map(int, row[2:])
    days_sum[i%7]+=row[2]
    i+=1
    if j<7:
        days.append(row[1])
        j+=1

import matplotlib.pyplot as plt
plt.rc("font",family="Magun Gothic")
