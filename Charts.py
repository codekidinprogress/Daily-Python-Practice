import matplotlib.pyplot as plt

sunny_days = [8, 10, 7, 14, 20, 18, 25, 19, 18, 14, 12, 7]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

avg_sunny_days = sum(sunny_days) / len(sunny_days)

plt.plot(months, sunny_days, marker="o", label="Sunny days")
plt.title("Sunny Days by Month", fontsize=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Sunny days", fontsize=14)
plt.axhline(avg_sunny_days, linestyle="--", color="orange", label="Average")
plt.legend()

plt.show()
