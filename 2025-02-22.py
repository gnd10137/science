import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
train = pd.read_csv("train.csv", parse_dates=["datetime"])
train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["day"] = train["datetime"].dt.day
train["hour"] = train["datetime"].dt.hour
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train["dayofweek"] = train["datetime"].dt.dayofweek
plt.style.use("ggplot")
plt.rc("font", family = "Malgun Gothic")
sns.pointplot(x = "hour", y= "count", data = train, hue = "holiday")
plt.show()
