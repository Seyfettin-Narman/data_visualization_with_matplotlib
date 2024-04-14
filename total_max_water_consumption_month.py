import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

df = pd.read_csv('izsu_su_tuketimi.csv', sep=';')

ilce_ay_ortalama = df.groupby(['ILCE', 'AY'])['ORTALAMA_TUKETIM'].mean().reset_index()
ilce_max_ay = ilce_ay_ortalama.loc[ilce_ay_ortalama.groupby('ILCE')['ORTALAMA_TUKETIM'].idxmax()]

colors = []
for _ in range(len(ilce_max_ay)):
    color = [random.uniform(0, 1) for _ in range(3)]
    colors.append(color)

plt.figure(figsize=(16, 10))

for i, ilce in enumerate(ilce_max_ay['ILCE']):
    plt.bar(ilce, ilce_max_ay.loc[ilce_max_ay['ILCE'] == ilce, 'ORTALAMA_TUKETIM'],
            color=colors[i], label=ilce,width=0.8)

plt.xlabel('İlçe')
plt.ylabel('Ortalama Su Tüketimi')
plt.title(' İzmirin Her Bir İlçesinin En Yüksek Su Tüketim Oranına Sahip Ayı ve Tüketimi (2015-2024)')
plt.xticks(rotation=45)
aylar = {1: 'OCAK', 2: 'ŞUBAT', 3: 'MART', 4: 'NİSAN', 5: 'MAYIS', 6: 'HAZİRAN', 7: 'TEMMUZ', 8: 'AĞUSTOS', 9: 'EYLÜL', 10: 'EKİM', 11: 'KASIM', 12: 'ARALIK'}

for i, ay in enumerate(ilce_max_ay['AY']):
    ay_adi = aylar.get(ay)
    plt.text(i, ilce_max_ay.iloc[i]['ORTALAMA_TUKETIM'] + 0.5, ay_adi, ha='center', va='bottom', fontsize=8)

max_tuketim = ilce_max_ay['ORTALAMA_TUKETIM'].max()
plt.yticks(np.arange(0, max_tuketim + 600, 200))
for y_degeri in np.arange(200, max_tuketim + 600, 200):
    plt.axhline(y=y_degeri, color='black', linestyle='--', linewidth=0.8)
plt.tight_layout()
plt.show()