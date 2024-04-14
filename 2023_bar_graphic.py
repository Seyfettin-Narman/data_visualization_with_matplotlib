import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('izsu_su_tuketimi.csv', sep=';')

df_2023 = df[df['YIL'] == 2023]
df_2023 = df_2023[['ILCE', 'ORTALAMA_TUKETIM']]

ilce_ortalama_tuketim = df_2023.groupby('ILCE')['ORTALAMA_TUKETIM'].mean()
plt.figure(figsize=(16, 10))

colors = plt.cm.tab20(np.arange(len(ilce_ortalama_tuketim)))

ilce_ortalama_tuketim.plot(kind='bar', color=colors)
plt.xlabel('İlçe')
plt.ylabel('Ortalama Su Tüketimi')
plt.title('İzmir İlçelerinin 2023 Yılı Ortalama Su Tüketimi')
plt.xticks(rotation=45)
max_value = int(max(ilce_ortalama_tuketim))
plt.yticks(range(0, max_value + 200, 200))

for y_degeri in np.arange(0, max_value + 200, 200):
    plt.axhline(y=y_degeri, color='black', linestyle='--', linewidth=0.8)

plt.tight_layout()
plt.show()