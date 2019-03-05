import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [10, 20, 30, 40, 50]

#plt.plot(squares)
plt.axis([0,100, 0, 100])

plt.scatter (input_values, squares, linewidth=5, c=input_values, cmap=plt.cm.Reds)
plt.title ("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel ("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=12)


plt.show()
