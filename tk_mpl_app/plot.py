import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
sunny_days = [8,10,7,14,20,18,25,19,18,14,12,7]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_sunny_days = sum(sunny_days) / len(sunny_days)

# -----------------------------
# Graph functions
# -----------------------------
def draw_line(fig):
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(months, sunny_days, marker='o', color='r', label='Sunny Days')
    ax.axhline(y=avg_sunny_days, linestyle='--', color='green', label='Average Sunny Days')
    ax.set_title('Sunny Days per Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sunny Days')
    ax.legend()

def draw_bar(fig):
    fig.clear()
    ax = fig.add_subplot(111)
    ax.bar(months, sunny_days, color='orange')
    ax.set_title('Sunny Days per Month - Bar Chart')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sunny Days')
