from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)


df2 = pd.read_csv("Samsung.KS.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
print(index2)


mean = df1["Close"].mean()


plt.figure("Apple")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="APPL Stock price, mean="+str(mean))
plt.plot(df1["Date"], df1["Close"], 'o', ms=1, markevery=index2, label="Apple")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()

print(plt.show())