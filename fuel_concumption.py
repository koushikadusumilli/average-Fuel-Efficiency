import pandas as pd

# Load the dataset
df = pd.read_csv("fuel_consumption_data.csv")

# Step 1: Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Step 2: Drop duplicate rows
df = df.drop_duplicates()
print("Duplicates removed. Current shape:", df.shape)

# Step 3: Convert data types
df['year'] = df['year'].astype(int)
df['engine_size'] = df['engine_size'].astype(float)
df['city_mpg'] = df['city_mpg'].astype(float)
df['highway_mpg'] = df['highway_mpg'].astype(float)
df['avg_mpg'] = df['avg_mpg'].astype(float)
df['date_logged'] = pd.to_datetime(df['date_logged'])

# Step 4: Identify and print outliers in avg_mpg (optional review)
outliers = df[(df['avg_mpg'] < 5) | (df['avg_mpg'] > 100)]
print(f"Outliers in avg_mpg: {len(outliers)} records")

# Step 5: Recalculate avg_mpg for consistency
df['avg_mpg'] = ((df['city_mpg'] + df['highway_mpg']) / 2).round(2)

# Save cleaned data to a new CSV
df.to_csv("cleaned_fuel_consumption_data.csv", index=False)
print("Cleaned data saved to 'cleaned_fuel_consumption_data.csv'")
