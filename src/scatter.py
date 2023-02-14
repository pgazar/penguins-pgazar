# this file create the scatter plot

import matplotlib.pyplot as plt
#importing function defined in dataProcess.py
from dataProcess import process

#importing function defined in readFile
from readFile import readit_all
# calling functions
data = readit_all()

x_label = "bill_length_mm"
y_label = "bill_depth_mm"
Y_label = "flipper_length_mm"
z_label = "species"

# calling functions
X, Y, Z = process(data, x_label, Y_label, z_label)

species = set([d[z_label] for d in data])
colormap = {s: ['tab:blue', 'tab:orange', 'tab:green'][i] for i,s in enumerate(species)}

for d in data:
    if d[x_label] == "NA" or d[y_label] == "NA":
        continue

    color = colormap[d[z_label]]
    plt.scatter(float(d[x_label]), float(d[y_label]), color=color)

plt.xlabel(x_label)
plt.ylabel(y_label)
plt.savefig('./img/1.png')
plt.close()
# creating the legend

for s in species:
 
  # another way that does the same thing as 2 lines above
  X_subset = [d for i, d in enumerate(X) if s == Z[i]]
  Y_subset = [d for i, d in enumerate(Y) if s == Z[i]]

  plt.scatter(X_subset, Y_subset, label=s)

plt.legend()
plt.xlabel(x_label)
plt.ylabel(Y_label)
plt.savefig('./img/2.png')
plt.close()
