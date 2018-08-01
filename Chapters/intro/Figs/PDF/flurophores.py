import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

fig = plt.figure(figsize=(4,4/1.618),frameon=True)
matplotlib.rc('pdf', fonttype=42)



cy5 = cereal_df = pd.read_csv('./fluorphores/Cy5.csv')
fluo = cereal_df = pd.read_csv('./fluorphores/Fluorescein (FITC).csv')
dapi = cereal_df = pd.read_csv('./fluorphores/DAPI.csv')
tr = cereal_df = pd.read_csv('./fluorphores/Texas Red.csv')
ax = plt.gca()
cy5.plot(x='Wavelength',y='Excitation',linestyle='-', color='red',stacked=False, label='Cy5 ex',ax=ax);
cy5.plot.area(x='Wavelength',y='Emission', ax=ax,linestyle='-', color='red',stacked=False,label='Cy5 em'):
fluo.plot(x='Wavelength',y='Excitation', ax=ax,linestyle='-', color='green',stacked=False,label='Fluorescein ex');
fluo.plot.area(x='Wavelength',y='Emission', ax=ax,linestyle='-', color='green',stacked=False,label='Fluorescein em');
tr.plot(x='Wavelength',y='Excitation', ax=ax,linestyle='-', color='orange',stacked=False,label='Texas red ex');
tr.plot.area(x='Wavelength',y='Emission', ax=ax,linestyle='-', color='orange',stacked=False,label='Texas red em');
dapi.plot(x='Wavelength',y='Excitation', ax=ax,linestyle='-', color='blue',stacked=False,label='DAPI ex');
dapi.plot.area(x='Wavelength',y='Emission', ax=ax,linestyle='-', color='blue',stacked=False,label='DAPI em');

ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.);


plt.xlim([300,800])
plt.ylabel('Relative intensity /%')
plt.xlabel('Wavelength /µm')
plt.tight_layout()

plt.savefig('./fluorphores/multi_plot.pdf',bbox_inches='tight')
plt.savefig('./fluorphores/multi_plot.png',bbox_inches='tight')
plt.show()
