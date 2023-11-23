import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a pandas DataFrame
df = pd.read_csv("cox-violent-parsed_filt_usable.csv")

# Data preprocessing
df['dob'] = pd.to_datetime(df['dob'], errors='coerce')  # Convert 'dob' column to datetime
df['screening_date'] = pd.to_datetime(df['screening_date'], errors='coerce')  # Convert 'screening_date' column to datetime
df['days_b_screening_arrest'] = pd.to_numeric(df['days_b_screening_arrest'], errors='coerce')  # Convert 'days_b_screening_arrest' to numeric
df['c_jail_in'] = pd.to_datetime(df['c_jail_in'], errors='coerce')  # Convert 'c_jail_in' column to datetime
df['c_jail_out'] = pd.to_datetime(df['c_jail_out'], errors='coerce')  # Convert 'c_jail_out' column to datetime

# Data analysis (you can perform your specific analysis here)

# Example: Calculate the average age by race
avg_age_by_race = df.groupby('race')['age'].mean()

# Plot the result
plt.figure(figsize=(10, 6))
avg_age_by_race.plot(kind='bar', color='skyblue')
plt.title('Average Age by Race')
plt.xlabel('Race')
plt.ylabel('Average Age')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as an image file !!!
plt.savefig('average_age_by_race.png')
plt.show()

#테스트한거 테스트추가인데
