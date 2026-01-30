import matplotlib.pyplot as plt

data = [22, 23, 25, 27, 28, 30, 31, 32, 35, 36]

plt.hist(data, bins=5)
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()
