import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Instance Hours.csv')

x1 = list(df.iloc[:, 0])
y1 = list(df.iloc[:, 1])
x2 = list(df.iloc[:, 3])
y2 = list(df.iloc[:, 4])

plt.plot(x2,y2, color='orange', label="Hours (Optimised)")
plt.bar(x1,y1, label="Hours (Normal)")
plt.legend()
plt.title("Instance Hours consumed (1 AMI)")
fig = plt.gcf()
fig.set_size_inches(8, 6)
fig.savefig('1ami.pdf')
plt.show()

df = pd.read_csv('Instance Hours.csv')

x1 = list(df.iloc[:, 6])
y1 = list(df.iloc[:, 7])
x2 = list(df.iloc[:, 9])
y2 = list(df.iloc[:, 10])

plt.plot(x2,y2, color='orange', label="Hours (Optimised)")
plt.bar(x1,y1, label="Hours (Normal)")
plt.legend()
plt.title("Instance Hours consumed (7 AMI)")
fig = plt.gcf()
fig.set_size_inches(8, 6)
fig.savefig('7ami.pdf', dpi=100)
plt.show()


df = pd.read_csv('Instance Hours.csv')

x1 = list(df.iloc[:, 12])
y1 = list(df.iloc[:, 13])
x2 = list(df.iloc[:, 15])
y2 = list(df.iloc[:, 16])

plt.plot(x2,y2, color='orange', label="Hours (Optimised)")
plt.bar(x1,y1, label="Hours (Normal)")
plt.legend()
plt.title("Instance Hours consumed (30 AMI)")
fig = plt.gcf()
fig.set_size_inches(12, 6)
fig.savefig('30ami.pdf', dpi=100)
plt.show()
