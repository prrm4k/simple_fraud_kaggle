import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('creditcard.csv')

df.head()

df.info()

df.isna().sum()

"""Видно, что у нескольких признаков присутствует одно пропущенное значение

Визаульно можно определить, что это последняя строка датафрейма

Удалим ее
"""

df.iloc[-1]

df = df.iloc[:-1]

"""Проведем визуальный анализ

"""

df.Time.plot()
plt.xlabel('Номер записи в датасете')
plt.ylabel('Количество секунд между операциями')
plt.title('Зависимость номера транзакции от времени между операциями')

fig, ax = plt.subplots(1, 2, figsize=(16,6))
ax[0].set_title('Анализ корреляций между 3мя признаками')
sns.heatmap(df[['Time', 'Amount','Class']].corr(), ax = ax[0])
sns.heatmap(df.corr(), ax = ax[1])
ax[1].set_title('Анализ корреляций между всеми признаками')

sns.distplot(df1.Time.values)
plt.xlim([min(df1.Time.values), max(df1.Time.values)])

"""# Проверим баланс классов"""

rat = len(df.Class)/sum(df.Class)
 rat

balanced_data = pd.concat([df.loc[df.Class==0], df.loc[df.Class==1].loc[df.loc[df.Class==1].index.repeat(rat)]] )

df1 = balanced_data.sample(frac=1).reset_index(drop=True)

df1.Class.value_counts()

"""# Когда классы сбалансированиы можно обучить модель"""

mod =HistGradientBoostingClassifier()

X_train, X_test, y_train, y_test =train_test_split(df1.drop(columns='Class'), df1.Class, test_size=0.3)

mod.fit(X_train, y_train)

ypr=mod.predict(X_test)

"""# Модель дала отличные результаты, но построим еще несколько моделей"""

precision_score(y_test, ypr)
