import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame, to_datetime

from src.emissions import get_dataframe


def mean_per_day(df: DataFrame) -> DataFrame:
    print(df['DatetimeBegin'].dtypes)
    df['DatetimeBegin'] = df['DatetimeBegin'].apply(lambda x: to_datetime(x))
    df['Date'] = df['DatetimeBegin'].apply(lambda x: x.date())
    df = df.groupby(["Countrycode", "AirPollutant", "UnitOfMeasurement", "Date"],
                    as_index=False)["mean o3 (µg/m3)"].mean()
    return df


df = get_dataframe("../../data/main/cleaned/mean/Amsterdam_o3_2013.csv")
mean_per_day(df)
# ax = sns.lineplot(x="DatetimeBegin", y="mean o3 (µg/m3)", data=df)
# plt.show()

