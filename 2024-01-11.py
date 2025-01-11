##from random import *
##a=[]
##
##for i in range(10):
##    a.append(randint(1,100))
##
##import numpy as np
##a=np.random.randint(1,101,100)

##import pandas as pd
##df =pd.read_html("https://ko.wikipedia.org/wiki/2023%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
##print(df)

##import pandas as pd
##
##df=pd.read_html("https://ko.wikipedia.org/wiki/2023%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
##print(df[0])

##import pandas as pd
##data={"name" :  ["펭수", "뽀로로", "뿡뿡이", "번개맨"],
##          "age" : [10,5,10,20],
##          "debut" : [2019,2003,2000,2000]}
##df=pd.DataFrame(data)
####print(df)
##
####print("1.", df.index)
####print("2.", df.columns)
####print("3.", df.values)
##
##print(df["name"])

##import pandas as pd
##
##df=pd.read_html("https://ko.wikipedia.org/wiki/2023%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
##week=pd.DataFrame(df[0])
##print(week["노래"])

##import pandas as pd
##
##df=pd.read_html("https://ko.wikipedia.org/wiki/2023%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
##week=pd.DataFrame(df[0])
##
##df_cnt=pd.DataFrame(week["노래"].value_counts())
##print(df_cnt)

##import pandas as pd
##import matplotlib.pyplot as plt
##
##df=pd.DataFrame( {"name" : ["펭수", "뽀로로", "뿡뿡이", "번개맨"],
##                                          "age" : [10,5,10,20]})
##plt.rc("font", family="Malgun Gothic")
##df.plot(x="name", y="age", kind="bar")
##plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_html("https://ko.wikipedia.org/wiki/2021%EB%85%84_%EA%B0%80%EC%98%A8_%EB%94%94%EC%A7%80%ED%84%B8_%EC%B0%A8%ED%8A%B8_1%EC%9C%84_%EB%AA%A9%EB%A1%9D")
week=pd.DataFrame(df[0])

df_cnt=pd.DataFrame(week["가수"].value_counts())
plt.rc("font", family="Malgun Gothic")
df_cnt.plot(kind="barh")
plt.show()
print(df_cnt)
