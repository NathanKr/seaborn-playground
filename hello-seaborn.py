import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn has built in data sets
print ("sns.get_dataset_names()\n",sns.get_dataset_names())
crash_df = sns.load_dataset('car_crashes')

# show the car crash data set  
# this is actually from https://www.kaggle.com/fivethirtyeight/fivethirtyeight-bad-drivers-dataset
print ("crash_df.shape : ",crash_df.shape)
print ("crash_df.head \n",crash_df.head())

# distribution plot
sns.displot(crash_df["total"])
plt.title("distribution plot")
plt.show()

# joint plot
sns.jointplot(x="speeding" , y="total",data=crash_df)
sns.jointplot(x="alcohol" , y="total",data=crash_df)
plt.title("joint plot")
plt.show()


# pairplot
sns.pairplot(crash_df)
plt.title("pair plot")
plt.show()







