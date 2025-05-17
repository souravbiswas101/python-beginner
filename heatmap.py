import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data_dic = {'A':[12,15,45,71],

            'B':[18,26,50,80],

            'C':[32,48,78,93],

            'D':[29,35,63,81]}

df = pd.DataFrame(data_dic)
sns.set_style('white')
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

