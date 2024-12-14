##import csv
##
##f=open("sns_use.csv", encoding="euc-kr")
##data=csv.reader(f)
##for row in data :
##    print(row)
##f.close()

##import csv
##f=open("sns_use.csv", encoding="euc-kr")
##data=csv.reader(f)
##header1=next(data)
##header2=next(data)
##print(header1)
##print(header2)
##f.close()

##import csv
##f=open("sns_use.csv", encoding="euc-kr")
##data=csv.reader(f)
##next(f)
##next(f)
##facebook=[]
##for row in data:
##    facebook.append(float(row[2]))
##print(facebook)
##f.close()

##import matplotlib. pyplot as plt
##plt.title("plotting")
##plt.plot([1,2,3,4], [10,20,30,40],color="red", label="asc")
##plt.plot([1,2,3,4], [40,30,20,10],color="blue", label="desc")
##plt.legend()
##plt.show()

import csv
import matplotlib.pyplot as plt

plt.rc("font",family="Malgun Gothic")
f=open("sns_use.csv", encoding="euc-kr")
data=csv.reader(f)
next(f)
next(f)

year=[2016,2017,2018]
facebook=[]
kakao=[]
instargram=[]
x=[]

for row in data :
    facebook.append(float(row[2]))
    kakao.append(float(row[3]))
    instargram.append(float(row[4]))
    x.append(float(row[8]))
f.close()

plt.title("facebook occupancy radio")
plt.plot(year,facebook,color='blue', label="facebook")
plt.plot(year,kakao,color='orange', label="kakao")
plt.plot(year,instargram,color='purple', label="instargram")
plt.plot(year,x,color='black', label="x")
plt.legend()
plt.xlabel("연도")
plt.ylabel("이용률")
plt.show()
