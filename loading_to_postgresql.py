import pandas as pd
import psycopg2

# Load the CSV data
csv_file = "C:/Users/koush/OneDrive/Desktop/Fuel_Consumption/cleaned_fuel_consumption_data.csv"
df = pd.read_csv(csv_file)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="fuel_consumption",
    user="postgres",            # change if different
    password="1234",   # replace with your actual password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert each row
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO fuel_data (manufacturer, model, year, fuel_type, engine_size,
                               city_mpg, highway_mpg, avg_mpg, region, date_logged)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['manufacturer'], row['model'], int(row['year']), row['fuel_type'],
        float(row['engine_size']), float(row['city_mpg']),
        float(row['highway_mpg']), float(row['avg_mpg']),
        row['region'], row['date_logged']
    ))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("Data successfully imported into PostgreSQL!")

