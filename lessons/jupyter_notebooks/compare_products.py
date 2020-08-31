import pandas as pd 
import matplotlib.pyplot as plt

# Load in
products = pd.read_csv('../../datasets/products_clean.csv')

# Only make the plot if there is no missing data
if products.isnull().values.any():
	print('There is missing data in the dataframe! Make sure to leave no missing values so the plot can be made!')
else:
	# Make a boxplot
	boxplot = products.boxplot('user_rating', by = 'product_id')
	boxplot.set_xlabel('')
	boxplot.set_title('Product Review Comparison')
	boxplot.set_ylabel('User Ratings')
	plt.suptitle('') 

	# Save the boxplot
	plt.savefig('product_chart.png')
