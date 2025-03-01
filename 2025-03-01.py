import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rc("font", family="Malgun Gothic")

call_df = pd.read_csv("Calldata_2008.csv", encoding = "utf-8",parse_dates = ["일자(YYYYMMDD)"])
call_df.columns = ["일자","연령","성별","발신지1","발신지2","대분류","중분류","통화비율"]

rain_df = pd.read_csv("Raindata_2008.csv", encoding = "cp949",parse_dates = ["일시"])
rain_df.columns = ["지점번호","지점명","일자","강수량","1시간최대강수량","1시간최대강수량시각"]

is_true = (call_df["발신지1"]=="서울") & (call_df["대분류"]=="음식점")
call_df = call_df[is_true]
##print(call_df["중분류"].unique())
call_df = call_df.drop(columns = ["연령","성별","발신지1","발신지2","통화비율","대분류"])
rain_df = rain_df.drop(columns = ["지점번호","지점명","1시간최대강수량","1시간최대강수량시각"])
rain_df["강수량"] = rain_df["강수량"].fillna(0)

tot_df = pd.merge(call_df,rain_df,on="일자")
no_rain = tot_df[tot_df["강수량"] == 0]
no_rain = pd.DataFrame(no_rain["중분류"].value_counts())

yes_rain = tot_df[tot_df["강수량"] >= 50]
yes_rain = pd.DataFrame(yes_rain["중분류"].value_counts())

##plt.rc("font", size=20)
##plt.rcParams["figure.figsize"] = (20,10)
##sns.countplot(data = tot_df, x = "강수량", hue = "중분류")
##plt.legend(loc = "upper right")
##plt.show()

color = ["royalblue", "orange", "crimcon", "forestgreen", "chocolate", "tomato"]
yes_rain.plot.pie(autopct="%.2f",subplots=True,colors=color)
plt.show()
