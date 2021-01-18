import seaborn as sns
import matplotlib.pyplot as plt


tips_df = sns.load_dataset('tips')
print("tips_df.shape : ",tips_df.shape)
print ("tips_df.head \n",tips_df.head())

# category plot
sns.catplot(x="day", y="total_bill", data=tips_df)
plt.title("category plot")
plt.show()


# multiples plot
g = sns.FacetGrid(tips_df, col="time")
g.map(sns.histplot, "tip")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('multiples plot')
plt.show()


