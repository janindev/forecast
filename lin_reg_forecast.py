# Linear regression with Python
# https://realpython.com/linear-regression-in-python/
#
# Using numpy and scikit-learn


import numpy as np
from sklearn.linear_model import LinearRegression

x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)                        # Obtain R2 score 

print('coefficient of determination:', r_sq)    
print('intercept:', model.intercept_)           # Obtain intercept b0
print('slope:', model.coef_)                    # Obtain coefficient b1, b2, bi


y_pred = model.predict(x)                       # Obtain predicted response
                                                # Same: y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)

print('predicted response:', y_pred, sep='\n')

# Apply model to new data
x_new = np.arange(10).reshape((-1, 2))          # np.arange creates an array: np.arange([start, ]stop, [step, ], dtype=None)
y_new = model.predict(x_new)
print(y_new)
