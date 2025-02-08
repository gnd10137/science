##import pandas as pd
##import matplotlib.pyplot as plt
##
##df=pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[1]
##df=pd.DataFrame(df)
####print(df.index)
####print(df.columns)
####print(df.sort_values(by="남성", ascending = True).head(5))
##
##df_m_avg=df["남성"].mean()
##df_w_avg=df["여성"].mean()
##
##print("Men :", df_m_avg)
##print("Women :", df_w_avg)
##
##diff = abs(df_m_avg - df_w_avg)
##
##if df_m_avg > df_w_avg:
##    gender1, gender2 = "men", "women"
##else :
##    gender1, gender2 = "women", "men"
##
##print("On anerge, %s live %.2f years longer than %s." % (gender1, diff, gender2))

##import pandas as pd
##import matplotlib.pyplot as plt
##import seaborn as sns
##plt.rc("font",family="Malgun Gothic")
##
##data1 = {"subject" : ["국어", "영어", "수학", "코딩"],
##                 "score" : [80,85,90,100]}
##ex_df1 = pd.DataFrame(data1)
##sns.barplot(data = ex_df1, x = "subject", y = "score")
##plt.show()

##import pandas as pd
##import matplotlib.pyplot as plt
##df=pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[1]
##df=pd.DataFrame(df)
##import seaborn as sns
##plt.rc("font", family="Malgun Gothic")
##df_m_sort=df.sort_values(by="남성", ascending=False).head(10)
##sns.barplot(data=df_m_sort, x="국가/영토", y="남성")
##plt.xticks(rotation=45)
##plt.ylim(70, 90)
##plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_html("https://ko.wikipedia.org/wiki/%EA%B8%B0%EB%8C%80%EC%88%98%EB%AA%85%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D")[1]
df=pd.DataFrame(df)

plt.rc("font", family="Malgun Gothic")
sns.scatterplot(data=df, x="남성", y="여성")
plt.xlim(45,90)
plt.ylim(45,90)
plt.plot([45,90], [45,90],'r')
plt.tight_layout()
plt.show()
