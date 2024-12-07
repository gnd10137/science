##f=open("Alice.txt", "r", encoding="UTF8")
##book=f.read()
##print(book)
##f.close()

##f=open("Alice.txt", "r", encoding="UTF8")
##book =f.read()
##count=book.count("앨리스")
##print(count)
##f.close()

##List=[1,3,5,7,[9,10]]
##for i in List:
##    print(i)

##List=[1,3,5,7,[9,10]]
##for i in range(len(List)):
##    print(List[i])

##import random
##List=[]
##
##for _ in range(10):
##    List.append(random.randint(1, 10))
##
##print(List)
##print(List.count(7))
##List.sort()
##print(List)
##List.reverse()
##print(List)

##list=[]
##while True:
##    n = int(input())
##    if n<0:
##        break
##    list.append(n)
##    list.sort()
##print(list)

##f=open("Alice.txt", "r", encoding="UTF8")
##book=f.read()
##words=input("검색하려고 하는 단어를 5개 입력해 주세요 :")
##words=words.split()
##for word in words :
##    n=book.count(word)
##    print("%s : %d번" %(word, n))
##f.close()


##f=open("Alice.txt", "r", encoding="UTF8")
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
##import matplotlib. pyplot as plt
##plt.rc("font", family="Malgun Gothic")
##plt.title("단어 개수")
##plt.plot(words, cnt)
##plt.show()

f=open("Alice.txt", "r", encoding="UTF8")
book=f.read()
words=input("검색하려고 하는 단어를 5개 입력해 주세요 :")
words=words.split()
cnt=[]

for word in words :
    n=book.count(word)
    cnt.append(n)
f.close()

import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
plt.title("단어 검색 결과")
plt.xlabel("검색 단어")
plt.ylabel("단어 개수")
plt.bar(words, cnt)
plt.show()
