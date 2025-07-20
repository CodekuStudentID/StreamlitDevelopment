import numpy as np 
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
                    11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0])

y_train = np.array([300.0, 320.0, 350.0, 370.0, 400.0, 420.0, 450.0, 470.0, 500.0, 520.0,
                    550.0, 570.0, 600.0, 620.0, 650.0, 670.0, 700.0, 720.0, 750.0, 770.0])

print(x_train)
print(y_train)

plt.scatter(x_train, y_train)
plt.show()