import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('izsu_su_tuketimi.csv', sep=';')

df_2023 = df[df['YIL'] == 2023]
df_2023 = df_2023[['ILCE', 'ORTALAMA_TUKETIM']]

ilce_ortalama_tuketim = df_2023.groupby('ILCE')['ORTALAMA_TUKETIM'].mean()
plt.figure(figsize=(12, 8))
ilce_ortalama_tuketim.plot(kind='pie', autopct='%1.1f%%', colors=plt.cm.tab20.colors)

plt.title('İzmir İlçelerinin 2023 Yılı Ortalama Su Tüketimi Dağılımı')
plt.ylabel('')
plt.tight_layout()
plt.show()