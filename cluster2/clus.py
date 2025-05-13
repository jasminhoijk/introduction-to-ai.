import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.cluster import KMeans  
from sklearn.preprocessing import StandardScaler 

df = pd.read_csv('CC GENERAL.csv')

# Удаляем строки с пропусками в числовых признаках
numeric_columns = ["BALANCE", "PURCHASES", "ONEOFF_PURCHASES", "INSTALLMENTS_PURCHASES", 
                   "CASH_ADVANCE", "PURCHASES_FREQUENCY", "ONEOFF_PURCHASES_FREQUENCY", 
                   "PURCHASES_INSTALLMENTS_FREQUENCY", "CASH_ADVANCE_FREQUENCY", 
                   "CASH_ADVANCE_TRX", "PURCHASES_TRX", "CREDIT_LIMIT", "PAYMENTS", 
                   "MINIMUM_PAYMENTS", "PRC_FULL_PAYMENT", "TENURE"]
df = df.dropna(subset=numeric_columns)

df = df[df["BALANCE"] >= 0]
df = df[df["PURCHASES"] >= 0] #отрицательные покупки

X = df.select_dtypes(include='number')

# Масштаб данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Финальная модель
k_opt = 3  
kmeans = KMeans(n_clusters=k_opt, random_state=10000)
df['Cluster'] = kmeans.fit_predict(X_scaled) # fit_predict

# Создаем категориальный признак на основе PRC_FULL_PAYMENT
df['Payment_Status'] = df['PRC_FULL_PAYMENT'].apply(lambda x: 'Full Payment' if x > 0 else 'Partial/No Payment')

# Печать кластеров и признаков
print("\nДанные с кластерами и признаками:")
print(df[['Cluster', 'BALANCE', 'PURCHASES', 'CREDIT_LIMIT', 'PAYMENTS', 'Payment_Status']])

# Подготовка данных точек для визуализации
points = df[['BALANCE', 'PURCHASES', 'Cluster', 'Payment_Status']].copy()
print("\nДанные точек для графика (BALANCE, PURCHASES, Cluster, Payment_Status):")
print(points.head(10))

# Визуализация на паре признаков (BALANCE vs PURCHASES)
sns.scatterplot(data=df, x='BALANCE', y='PURCHASES', hue='Cluster', palette='Set2', s=100)
plt.title('Кластеры клиентов по балансу и покупкам')
plt.xlabel('Balance')
plt.ylabel('Purchases')
plt.grid()
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()