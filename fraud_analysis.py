import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/n10652388/OneDrive - Queensland University of Technology/CV/Work/Github/Python/project/financial_fraud_detection_dataset.csv")

# Print first few rows to confirm it's loaded
print(df.head())

# Print summary statistics (count, mean, std, min, max, and quartiles) for each numerical column 
print(df.describe())

print(df.info())

# drop null values
df.dropna(inplace=True)

# Display the names of all columns in the DataFrame
df.columns

#rename column
df.rename(columns={"merchant_category":"merchant_type"})

# use describe() for specific columns
df[['transaction_type','location', 'device_used']].describe()


# plotting a bar chart for location and it's count

ax = sns.countplot(x = 'location',data = df)

for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()

 # This plot reveals which merchant types have higher spending

amount_merchant_type = df.groupby(['merchant_category'], as_index=False)['amount'].sum().sort_values(by='amount', ascending=False)
sns.barplot(x = 'merchant_category',y= 'amount' ,data = amount_merchant_type)
plt.xticks(rotation=45)
plt.show()

# Plotting the count of fraudulent vs. non-fraudulent transactions
sns.countplot(x='is_fraud', data=df)
plt.title('Fraudulent vs. Non-Fraudulent Transactions')
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.show()

# Calculating and plotting the average transaction amount by transaction type
avg_amount_type = df.groupby('transaction_type')['amount'].mean().reset_index().sort_values(by='amount', ascending=False)

sns.barplot(x='transaction_type', y='amount', data=avg_amount_type)
plt.title('Average Transaction Amount by Type')
plt.xticks(rotation=45)
plt.show()

# Counting and plotting the number of fraud cases by location
fraud_by_location = df[df['is_fraud'] == 1].groupby('location').size().reset_index(name='fraud_count').sort_values(by='fraud_count', ascending=False)

sns.barplot(x='location', y='fraud_count', data=fraud_by_location)
plt.title('Fraud Count by Location')
plt.xticks(rotation=45)
plt.show()

# Boxplot showing the distribution of time since last transaction for fraud and non-fraud cases
sns.boxplot(x='is_fraud', y='time_since_last_transaction', data=df)
plt.title('Time Since Last Transaction: Fraud vs Non-Fraud')
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.show()


# Validate fraud labels
print(df['is_fraud'].value_counts(dropna=False))
print(df['is_fraud'].unique())

df = pd.read_csv(
    "C:/Users/n10652388/OneDrive - Queensland University of Technology/CV/Work/Github/Python/project/financial_fraud_detection_dataset.csv",
    converters={'is_fraud': lambda x: x == 'True'}
)

# Show the first few actual values in the 'is_fraud' column
print(df['is_fraud'].unique())
print(df['is_fraud'].value_counts())



# Countplot of fraud vs. non-fraud
sns.countplot(x='is_fraud', data=df)
plt.title("Fraudulent vs. Non-Fraudulent Transactions")
plt.xticks([0, 1], ['Not Fraud', 'Fraud'])
plt.ylabel("Number of Transactions")
plt.xlabel("Transaction Type")
plt.show()

