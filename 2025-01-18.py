##import pandas as pd
##df=pd.read_csv("fruit.csv", encoding="euc-kr")
##print(df.head())

##import pandas as pd
##df=pd.read_csv("seoul.csv", encoding="euc-kr")
##print(df)

##import pandas as pd
##df=pd.read_csv("fruit.csv", encoding="euc-kr")
##print("# 최댓값 출력\n", df.max())
##print("# 최솟값 출력\n", df.min())
####print("# 평균값 출력\n", df.mean())

##import pandas as pd
##df=pd.read_csv("fruit.csv", encoding="euc-kr")
##print(df["수량"].idxmax(), df["수량"].idxmin())
##print(df.loc[df["수량"].idxmax()])

##import pandas as pd
##df=pd.read_csv("seoul.csv", encoding="euc-kr")
##print(df.loc[df["최고기온"].idxmax()])

##import pandas as pd
##name=input()
##df=pd.read_csv("fruit.csv",encoding="euc-kr")
##print(df[df["과일명"].str.contains(name)])

##import pandas as pd
##name=input()
##df=pd.read_csv("seoul.csv",encoding="euc-kr")
##print(df[df["년월"].str.contains(name)])

##import pandas as pd
##df=pd.read_csv("fruit.csv", encoding="euc-kr")
##print(df.sort_values(by = "금액", ascending=False).head(3))

##import pandas as pd
##df=pd.read_csv("seoul.csv", encoding="euc-kr")
##print(df.sort_values(by = "최저기온", ascending=True).head(5))

##import pandas as pd
##df=pd.read_csv("seoul.csv",encoding="euc-kr")
##print(df.loc[df["평균기온"].idxmax()])

##import pandas as pd
##df=pd.read_csv("seoul.csv",encoding="euc-kr")
##print(df.loc[df["평균기온"].idxmin()])

##import pandas as pd
##df=pd.read_csv("seoul.csv",encoding="euc-kr")
##print(df.sort_values(by="평균기온", ascending=False).head(5))

##import pandas as pd
##df=pd.read_csv("seoul.csv",encoding="euc-kr")
##print(df.sort_values(by="평균기온", ascending=True).head(5))

##import pandas as pd
##
##df=pd.read_csv("seoul.csv", encoding="euc-kr")
##df.columns=["년월", "평균기온", "최저기온", "최고기온"]
##
##df2=df[df["년월"].str.contains(" 1월")]
##jan_avg=df2["평균기온"]
##
##df2=df[df["년월"].str.contains("8월")]
##aug_avg=df2["평균기온"]
##
##print(jan_avg)
##print(aug_avg)

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("seoul.csv", encoding="euc=kr")
df.columns=["년월", "평균기온", "최저기온", "최고기온"]
df2=df[df["년월"].str.contains(" 1월")]

plt.rc("font", family="Malgun Gothic")
plt.rcParams["axes.unicode_minus"]=False
df2.plot(x="년월", y="평균기온", title= "2011-2020년 1월의 평균기온 변화 그래프")
plt.show()
