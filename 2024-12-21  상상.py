##f=open("Alicee.txt", "r", encoding="UTF8")
##book=f.read()
##print(book)
##f.close()

##str = "out of sight, out of mind"
##n = str.count("out")
##print('out : %d개' % n)

##List = [1,3,5,7,[9,10]]
##for i in List :
##    print(i)

##List = [1,3,5,7,[9,10]]
##for i in range(len(List)) :
##    print(List[i])

##import random
##List = []
##
##for _ in range(10) :
##    List.append(random.randint(1,10))
##
##print(List)
##print(List.count)
##List.sort()
##print(List)
##List.reverse()
##print(List)

##f = open("Alicee.txt","r",encoding = "UTF8")
##book=f.read()
##words=input("검색하려고 하는 단어를 5개 입력해 주세요 : ")
##words=words.split()
##for word in words :
##    n=book.count(word)
##    print("%s : %d번" %(word, n))
##f.close()

##f=open("Alicee.txt", "r", encoding = "UTF8")
##book = f.read()
##words = input("검색하려고 하는 단어를 5개 입력해 주세요 :")
##words = words.split()
##cnt=[]
##
##for word in words :
##    n = book.count(word)
##    cnt.append(n)
##f.close()
##
##import matplotlib.pyplot as plt
##plt.rc("font", family = "Malgun Gothic")
##plt.title("단어 개수")
##plt.plot(words, cnt)
##plt.show()

##f=open("Alicee.txt","r", encoding="UTF8")
##book=f.read()
##words=input("검색하려고 하는 단어를 5개 입력해 주세요 :")
##words=words.split()
##cnt=[]
##
##for word in words :
##    n=book.count(word)
##    cnt.append(n)
##f.close()
##
##import matplotlib.pyplot as plt
##plt.rc("font", family="Malgun Gothic")
##plt.title("단어 검색 결과")
##plt.xlabel("검색 단어")
##plt.ylabel("단어 개수")
##plt.bar(words, cnt)
##plt.show()

##import csv
##
##f=open("report.txt", encoding="UTF8")
##data=csv.reader(f)
##
##for row in data :
##    print(row)
##f.close()

##import csv
##
##f=open("report.txt", encoding="UTF8")
##data=csv.reader(f)
##header=next(data)
##print(header)
##f.close()

import matplotlib.pyplot as plt
plt.title("plotting")
plt.plot([1,2,3,4],[10,20,30,40],color="red",label="asc")
plt.plot([1,2,3,4],[40,30,20,10],color="blue",label="desc")
plt.legend()
plt.show()
