import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- LOAD DATA ----------------
df = pd.read_csv("electricity_bill_dataset.csv")
df = df.dropna()

# ---------------- GRAPH 1: Appliance Usage ----------------
appliances = ['Fan', 'Refrigerator', 'AirConditioner', 'Television', 'Monitor', 'MotorPump']
usage = df[appliances].mean()

plt.figure()
bars = usage.plot(kind='bar')

plt.title("Average Appliance Usage")
plt.xlabel("Appliances")
plt.ylabel("Average Usage")
plt.xticks(rotation=45)


for i, value in enumerate(usage):
    plt.text(i, value, f"{value:.1f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ---------------- GRAPH 2: Tariff vs Bill ----------------
plt.figure()
sns.scatterplot(x='TariffRate', y='ElectricityBill', data=df)

plt.title("Tariff Rate vs Electricity Bill")
plt.xlabel("Tariff Rate")
plt.ylabel("Electricity Bill")
 
max_row = df.loc[df['ElectricityBill'].idxmax()]
plt.annotate(
    "Highest Bill",
    (max_row['TariffRate'], max_row['ElectricityBill']),
    textcoords="offset points",
    xytext=(10,10),
    arrowprops=dict(arrowstyle="->")
)

plt.tight_layout()
plt.show()


# ---------------- GRAPH 3: Bill Distribution ----------------
plt.figure()
sns.histplot(df['ElectricityBill'], bins=30)

plt.title("Distribution of Electricity Bill")
plt.xlabel("Electricity Bill")
plt.ylabel("Frequency")

mean_val = df['ElectricityBill'].mean()
plt.axvline(mean_val, linestyle='--')
plt.text(mean_val, plt.ylim()[1]*0.9, f"Mean: {mean_val:.0f}")

plt.tight_layout()
plt.show()


# ---------------- GRAPH 4: Pie Chart ----------------
explode = [0.1 if val == usage.max() else 0 for val in usage]

plt.figure()
plt.pie(usage, labels=appliances, autopct='%1.1f%%', explode=explode)
plt.title("Appliance Contribution (Highlighted Highest Usage)")

plt.tight_layout()
plt.show()


# ---------------- GRAPH 5: City vs Average Bill ----------------
city_bill = df.groupby('City')['ElectricityBill'].mean()

plt.figure()
bars = city_bill.plot(kind='bar')

plt.title("Average Electricity Bill by City")
plt.xlabel("City")
plt.ylabel("Average Bill")
plt.xticks(rotation=45)

for i, value in enumerate(city_bill):
    plt.text(i, value, f"{value:.0f}", ha='center', va='bottom')

plt.tight_layout()
plt.show()


# ---------------- GRAPH 6: Heatmap ----------------
selected_cols = ['Fan', 'AirConditioner', 'Refrigerator', 'MonthlyHours', 'TariffRate', 'ElectricityBill']
corr = df[selected_cols].corr()

plt.figure()
sns.heatmap(corr, annot=True)

plt.title("Correlation Between Key Factors")

max_corr = corr.unstack().sort_values(ascending=False)
max_corr = max_corr[max_corr < 1].index[0]

plt.text(1, -0.5, f"Strongest: {max_corr}", fontsize=10)

plt.tight_layout()
plt.show()