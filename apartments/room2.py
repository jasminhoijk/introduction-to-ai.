import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

file_path = 'HousingPrices.csv'  
df = pd.read_csv(file_path)

# Drop rows where any of these columns have missing values
df = df.dropna(subset=['Area', 'Room', 'Price'])


scaler = StandardScaler()
df[['Area', 'Room']] = scaler.fit_transform(df[['Area', 'Room']])  # Scale Area and Room


X = df[['Area']].values  
Y = df['Price'].values

# divide into 2 groups test and trainе
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#регресся
model = LinearRegression()
model.fit(X_train, Y_train)

# Средняя цена
average_price = np.mean(Y)
print(f"Средняя цена: {average_price:.2f}")

# Разница между предсказаниями и средней ценой
delta_set = np.mean(np.abs(model.predict(X_test) - average_price))

# Accuracy
accuracy = r2_score(Y_test, model.predict(X_test))* 100

print(f"Точность модели: {accuracy:.2f}%")
print(f"Средняя цена: {np.mean(Y):.2f}")
print(f"Дельтасет (разница предсказания и средней цены): {delta_set:.2f}")

new_flat = np.array([[120]])  
pred_ml = model.predict(new_flat)[0]  
print(f"Предсказание (ML): {pred_ml:.2f}")

sorted_indices = np.argsort(X[:, 0])  
X_sorted = X[sorted_indices]  
Y_sorted = model.predict(X_sorted)

Y_sorted_centered = Y_sorted + (average_price - np.mean(Y_sorted))


plt.scatter(X[:, 0], Y, color='red', alpha=0.5, label='Реальные данные')
plt.plot(X_sorted[:, 0], Y_sorted_centered, color='blue', linewidth=2, label='Линейная регрессия')
plt.xlabel('Area (scaled)')
plt.ylabel('Price')
plt.legend()
plt.show()
