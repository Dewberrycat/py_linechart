import matplotlib.pyplot as plt

first = []
second = []
lines = int(input('Enter how many lines '))
steps = int(input('Enter how many steps '))
print()
for i in range(steps):
	new = int(input('X axis next element '))
	first.append(new)

for i in range(lines):
	for j in range(steps):
		new = int(input('Y axis of ' + str(i + 1) + ' next element '))
		second.append(new)
		if (j + 1) == steps:
			plt.plot(first, second)
			second = []

plt.show()





input()





