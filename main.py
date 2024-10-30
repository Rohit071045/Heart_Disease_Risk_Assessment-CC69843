import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv('CVD_cleaned.csv')

# Explore the data
print(df.head())  # Display the first few rows
print(df.info())  # Summary information
print(df.shape)
print(df.describe())

# Check the missing values
print(df.isna().sum())

# Check the duplicated values
print(df.duplicated().sum())

# Now let's remove duplicated values
duplicates = df.duplicated()
print(df[duplicates])
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

# Boxplot
plt.figure(figsize=(12, 8))
sns.boxplot(data=df)
plt.title('Boxplot of Features\n-Rohit Raj')
plt.show()

# Histogram
df.hist(figsize=(12, 8))
plt.suptitle('Histogram of Features\n-By Rohit Raj', y=0.95)
plt.show()

# List of columns
print(df.columns.tolist())

# Countplot for 'Sex'
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', data=df)
plt.title('Distribution of Gender\n-By Rohit Raj')
plt.show()

# Visualization on Age_Category
plt.figure(figsize=(10, 6))
plt.hist(df['Age_Category'], bins=20, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution\n-By Rohit Raj')
plt.show()

# Visualization between Green_Vegetables_Consumption vs. FriedPotato_Consumption
plt.figure(figsize=(10, 6))
plt.scatter(df['Green_Vegetables_Consumption'], df['FriedPotato_Consumption'])
plt.xlabel('Green Vegetables Consumption')
plt.ylabel('Fried Potato Consumption')
plt.title('Green Vegetables Consumption vs. Fried Potato Consumption\n-By Rohit Raj')
plt.show()

# Visualization of smoking history
smoking_data = {
    'Smoking_History': ['Yes', 'No'],
    'Count': [120, 80]
}
plt.figure(figsize=(8, 6))
sns.barplot(x='Smoking_History', y='Count', data=pd.DataFrame(smoking_data))
plt.title('Smoking History\n-By Rohit Raj')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.show()

# Histogram plot with multiple features
data = pd.DataFrame({
    'Age_Category': [25, 30, 35, 40, 45, 50],
    'BMI': [22.5, 24.0, 26.5, 28.2, 29.8, 31.0],
    'Weight_(kg)': [60, 65, 70, 75, 80, 85],
    'Height_(cm)': [165, 170, 175, 180, 185, 190]
})
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Age_Category', bins=10, kde=True, color='skyblue', label='Age Category')
sns.histplot(data=data, x='BMI', bins=10, kde=True, color='salmon', label='BMI')
sns.histplot(data=data, x='Weight_(kg)', bins=10, kde=True, color='green', label='Weight')
sns.histplot(data=data, x='Height_(cm)', bins=10, kde=True, color='purple', label='Height')
plt.xlabel('Values')
plt.ylabel('Density')
plt.title('Distribution of Age, BMI, Weight, and Height\n BY- -By Rohit Raj')
plt.legend()
plt.show()
