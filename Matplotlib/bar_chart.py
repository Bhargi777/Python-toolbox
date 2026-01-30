import matplotlib.pyplot as plt

categories = ["A", "B", "C", "D"]
values = [10, 25, 15, 30]

plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart Example")
plt.show()

