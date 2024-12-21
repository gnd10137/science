##import csv
##f=open("persons.csv",encoding="euc-kr")
##data=csv.reader(f)
##next(data)
##for row in data :
##    row[1 :]=map(int, row[1 :])
##    print(row)
##f.close()

##import csv
##f=open("persons.csv",encoding="euc-kr")
##data=csv.reader(f)
##next(data)
##area=input("동 단위로 검색 :")
##
##for row in data :
##    row[1 :]=map(int, row[1 :])
##    if area in row[0] :
##        print("남자 -", row[17:22])
##        print("여자 -", row[80:85])
##        break
##f.close()

##import csv
##import matplotlib.pyplot as plt
##f=open("persons.csv",encoding="euc-kr")
##data=csv.reader(f)
##next(data)
##area=input("구 단위로 검색 :")
##name=[]
##tot=[]
##
##for row in data :
##    row[1 :]=map(int, row[1 :])
##    sumB=0
##    sumG=0
##    if area in row[0] :
##        for i in range(17, 23) :
##            sumB += row[i]
##            sumG +=row[i+63]
##        name.append(row[0][:-12])
##        tot.append(sumB+sumG)
##print(name)
##print(tot)
##f.close()
##
##del name[0]
##del tot[0]
##
##plt.rc("font", family="Malgun Gothic")
##plt.title("%s 청소년 인구 수" % area)
##plt.barh(name,tot,color="green")
##plt.show()
##plt.rc("font", family="Malgun Gothic")
##plt.barh(['월','화','수','목','금'], [110,80,93,42,70])
##plt.show()

##import matplotlib.pyplot as plt
##import random
##m=[]
##f=[]
##
##for i in range(100) :
##    m.append(random.randint(0, 99))
##    f.append(random.randint(0, 99)*-1)
##plt.barh(range(100), m)
##plt.barh(range(100), f)
##plt.show()

import matplotlib.pyplot as plt
import csv
f=open("persons.csv",encoding="euc-kr")
data=csv.reader(f)
next(data)

men=[]
women=[]
area=input("동 단위로 검색  : ")

for row in data :
    row[1 :]=map(int, row[1 :])
    if area in row[0] :
        for i in range(3,64) :
            men.append(row[i]*-1)
            women.append(row[i+63])
        break
f.close()

plt.rc("font", family="Malgun Gothic")
plt.rcParams["axes.unicode_minus"]=False
plt.title("%s  남녀 인구수" % area)
plt.barh(range(61),men,color="green",label="남자")
plt.barh(range(61),women,color="orange",label="여자")
plt.legend()
plt.show()
