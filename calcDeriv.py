import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

ws = load_workbook("log data.xlsx")["sheet"]
max_row = ws.max_row

data = []
for i in range(1, max_row + 1) :
    data.append([ ws[f"A{i}"].value , ws[f"B{i}"].value ])

data = np.array(data)

x = data[:, 0]
y = data[:, 1]

dy = y[1:] - y[:-1]
dx = x[1:] - x[:-1]
deriv = dy/dx

ddy = dy[1:] - dy[:-1]
second_deriv = ddy/dx

plt.plot(x, y, label="log")
plt.plot(x[:-1], deriv, label="1st deriv")
plt.plot(x[:-2], second_deriv, label="2nd deriv")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()