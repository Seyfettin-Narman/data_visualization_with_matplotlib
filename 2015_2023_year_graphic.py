import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('izsu_su_tuketimi.csv', sep=';')
ilce_yillara_gore_tuketim = df.groupby(['ILCE', 'YIL'])['ORTALAMA_TUKETIM'].mean().unstack()

ilce_yillara_gore_tuketim = ilce_yillara_gore_tuketim.loc[:, :2023]
fig, ax = plt.subplots(figsize=(18, 10))

renkler = {
    2015: 'purple',
    2016: 'red',
    2017: 'navy',
    2018: 'pink',
    2019: 'blue',
    2020: 'orange',
    2021: 'green',
    2022: 'yellow',
    2023: 'turquoise'
}

renk_listesi = [renkler[yil] for yil in ilce_yillara_gore_tuketim.columns]
ilce_yillara_gore_tuketim.plot(kind='bar', color=renk_listesi, ax=ax, width=0.6)

ax.set_xlabel('Yıl')
ax.set_ylabel('Ortalama Su Tüketimi')
ax.set_title('İzmir İlçelerinin Yıllara Göre(2015-2023) Ortalama Su Tüketimi')
ax.tick_params(axis='x', rotation=45)

max_tuketim = ilce_yillara_gore_tuketim.max().max()
ax.set_yticks(np.arange(0, max_tuketim + 200, 200))
for y_degeri in np.arange(200, max_tuketim + 200, 200):
    ax.axhline(y=y_degeri, color='black', linestyle='--', linewidth=0.8)

ax.legend(title='YIL', fontsize='small')
plt.tight_layout()
plt.show()