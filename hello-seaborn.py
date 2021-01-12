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
print ("crash_df.shape \n",crash_df)

# distribution plot
sns.displot(crash_df["total"])
plt.show()

# joint plot
sns.jointplot(x="speeding" , y="total",data=crash_df)
sns.jointplot(x="alcohol" , y="total",data=crash_df)
plt.show()


# pairplot
sns.pairplot(crash_df)
plt.show()







