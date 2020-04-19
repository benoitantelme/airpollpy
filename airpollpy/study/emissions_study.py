import seaborn as sns
import matplotlib.pyplot as plt
from src.emissions import get_dataframe, mean_per_day

df = get_dataframe("../../data/main/cleaned/mean/Amsterdam_o3_2013.csv")
mean_per_day(df)
sns.set_style("whitegrid", {'grid.linestyle': '-'})
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x="DatetimeBegin", y="mean o3 (µg/m3)", data=df).set_title('Amsterdam o3 emissions 2013')

plt.show()

