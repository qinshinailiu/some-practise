import pandas as pd 
from sklearn.model_selection import train_test_split

data = pd. read_csv('melb_data.csv')

cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]
y = data.Price

X_train, X_valid, y_train, y_valid = train_test_split(X, y)

from xgboost import XGBRegressor

"""docstring
n_estimators 表示循环次数（模型个数 一般在100-1000之间
early_stopping_rounds 
learning_rate 学习率
n_jobs 多线程？
"""
my_model = XGBRegressor(n_estimators = 500,learning_rate=0.05,n_jobs = 4)
my_model.fit(X_train,y_train,
			early_stopping_rounds = 5,
			eval_set=[(X_valid,y_valid)],
			verbose = False
			)

from sklearn.metrics import mean_absolute_error
predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))