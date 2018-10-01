import matplotlib.pyplot as plt
import seaborn as sns

mpg = sns.load_dataset("mpg") # Load the example mpg dataset

sns.relplot(x="horsepower", y="mpg", hue="origin", size="weight",
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg) # Plot miles per gallon against horsepower with other semantics
plt.show()