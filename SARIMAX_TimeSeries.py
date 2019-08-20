import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Data
df = pd.read_csv('E:\\OneDrive\\AmateurWork\\Python\\Udemy\\TimeSeries\\TSA_COURSE_NOTEBOOKS\\Data\\HospitalityEmployees.csv', index_col = 'Date', parse_dates=True)
df.head()
df.index.freq = 'MS'
print(len(df))
print(df.shape)
# Create chart to see distribution
df['Employees'].plot()
plt.show()

# Plot to see Trend, Seasons and residual distribution
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['Employees'])
result.plot()
plt.show()

result.seasonal.plot()
plt.show()

# The distribution has seasonal part in it.
# We shall run pmd auto-arima to get the orderes

from pmdarima import auto_arima
auto_arima(df['Employees'], seasonal=True, max_p=2, max_q=2, max_d=2, m=12).summary()

Ltrain = 12
train = df[:-Ltrain]
test = df[-Ltrain:]

from statsmodels.tsa.statespace import sarimax
result = sarimax.SARIMAX(train['Employees'], order = (1, 1, 2), seasonal_order = (1, 0, 1, 12), enforce_invertibility = False).fit()
result.summary()
prediction = result.predict(start = len(train), end = len(df) - 1, type = 'levels').rename('SARIMA (1, 1, 2')

ax = df['Employees'].plot(legend = True)
prediction.plot(legend = True)
plt.show()

len(test)
len(prediction)
from statsmodels.tools.eval_measures import rmse
rmse(test['Employees'], prediction)
test['Employees'].mean()
prediction.mean()

# Predict for next one year
# Fit the model with whole dateset
result = sarimax.SARIMAX(df['Employees'], order = (1, 1, 2), seasonal_order = (1, 0, 1, 12), enforce_invertibility = False).fit()
result.summary()
# Prediction for 12 months ahead in time
prediction = result.predict(len(df), len(df)+12).rename('SARIM(1, 1, 2 - 12 Month')
df['Employees'].plot(legend = True)
prediction.plot(legend  = True)
plt.show()