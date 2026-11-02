"""Project : NGO Project Budget and Activity Tracking"""

import pandas as pd
import numpy as np

records = [
    {'activity': 'Training', 'planned_budget_kes': 150000, 'actual_spend_kes': 142000, 'planned_outputs': 10, 'actual_outputs': 9},
    {'activity': 'Community visits', 'planned_budget_kes': 90000, 'actual_spend_kes': 96000, 'planned_outputs': 30, 'actual_outputs': 34},
    {'activity': 'Materials', 'planned_budget_kes': 120000, 'actual_spend_kes': 113500, 'planned_outputs': 500, 'actual_outputs': 470},
    {'activity': 'Staff workshops', 'planned_budget_kes': 80000, 'actual_spend_kes': 73500, 'planned_outputs': 4, 'actual_outputs': 4},
    {'activity': 'Follow-up calls', 'planned_budget_kes': 45000, 'actual_spend_kes': 51000, 'planned_outputs': 300, 'actual_outputs': 270},
    {'activity': 'Monitoring visits', 'planned_budget_kes': 100000, 'actual_spend_kes': 94000, 'planned_outputs': 20, 'actual_outputs': 18},
    {'activity': 'Public awareness', 'planned_budget_kes': 70000, 'actual_spend_kes': 66500, 'planned_outputs': 8, 'actual_outputs': 9},
    {'activity': 'Data collection', 'planned_budget_kes': 60000, 'actual_spend_kes': 62500, 'planned_outputs': 6, 'actual_outputs': 6},
]

df = pd.DataFrame(records)

print("First five rows:")
print(df.head())

print("\nData shape:")
print(df.shape)



# 1. Check for missing values and ensure budget/spend/output columns are numeric.
print("\nMissing values:")
print(df.isna().sum())

print(df.dtypes)

# 2. Create budget_variance_kes = actual_spend_kes - planned_budget_kes.
df["budget_variance"] = df["actual_spend_kes"] - df["planned_budget_kes"]
# 3. Create budget_variance_pct = budget_variance_kes / planned_budget_kes * 100.
df["budget_variance_pct"] =round( df["budget_variance"] / df["planned_budget_kes"] * 100,2)


# 4. Create output_delivery_pct = actual_outputs / planned_outputs * 100.
df["output_delivery_pct"] =round( df["actual_outputs"] / df["planned_outputs"] * 100,2)

# 5. Label each activity 'Over budget' or 'Within/under budget'.
df["budget_status"] = np.where(df["budget_variance"] > 0, "Over budget", "Within/under budget")

print(df.round(1))
# 6. Identify activities that overspent and delivered less than 100% of planned outputs.
print(df[(df["budget_variance"] > 0) & (df["output_delivery_pct"] < 100)])




# 7. Calculate total planned budget, actual spend, and total budget variance.
print("Planned budget:", df["planned_budget_kes"].sum())


print("Actual spend:", df["actual_spend_kes"].sum())


print("Total variance:", df["actual_spend_kes"].sum() - df["planned_budget_kes"].sum())



# 8. Calculate overall output delivery using total actual outputs divided by total planned outputs.

print("Overall output delivery %:", round(df["actual_outputs"].sum()/df["planned_outputs"].sum()*100, 1))
#9.Create a horizontal bar chart of budget variance by activity.
plt.figure(figsize=(9, 5))
plt.barh(df["activity"], df["budget_variance"])
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("Budget variance (KES): actual - planned")
plt.ylabel("Activity")
plt.title("Budget variance by activity")
plt.tight_layout()
plt.savefig("barh.png")
plt.show()


# 10. Why spending alone does not show performance
# - Underspending can mean activities were delayed, cut or under-delivered
#   (e.g. Training and Monitoring visits underspent but delivered only 90% of outputs).
# - Overspending can be justified if it bought extra results
#   (e.g. Community visits overspent by 6.7% but delivered 113.3% of planned outputs).
# - Budget variance must be read together with output delivery.

# 11. Management summary (fictional data, for practice only)
# Finding 1: Total spend was KES 699,000 against a budget of KES 715,000
#            (KES 16,000 or 2.2% under), but overall output delivery was only 93.4%.
# Finding 2: Follow-up calls was the only activity that overspent (+13.3%)
#            and under-delivered (90% of planned outputs).
# Question 1: Why did follow-up calls cost more per call than planned?
# Question 2: Did Training and Monitoring visits underspend because of delays or cuts?
# Limitation: Fictional data; findings do not describe a real programme.

