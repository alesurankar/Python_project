import matplotlib.pyplot as plt

# Sample data
sunny_days = [8,10,7,14,20,18,25,19,18,14,12,7] 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

avg_sunny_days = sum(sunny_days) / len(sunny_days)

plt.plot(months, sunny_days, marker='o', color='r', label='Sunny Days')
plt.title('Sunny Days per Month', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sunny Days', fontsize=14)

plt.axhline(y=avg_sunny_days, linestyle='--', color='green', label='Average Sunny Days')
plt.legend()

plt.show()
