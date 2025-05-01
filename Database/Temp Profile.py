import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'D:/iCloudDrive/Sem 4/AAPG IBA 2025/Data/Provided Data/Newberry Data Set/Wells/well_temp.csv'  # Replace with your actual file name
df = pd.read_csv(file_path)

# Group by Well ID
grouped = df.groupby('Well ID')

# Plotting
plt.figure(figsize=(8, 10))

for well_id, group in grouped:
    group_sorted = group.sort_values('Depth')

    # If only one data point, assume surface temp = 0 at depth = 0
    if len(group_sorted) == 1:
        temp_profile = pd.DataFrame({
            'Depth': [0, group_sorted['Depth'].values[0]],
            'Temp': [0, group_sorted['Temp'].values[0]]
        })
    else:
        temp_profile = group_sorted

    plt.scatter(temp_profile['Temp'], temp_profile['Depth'], label=f'Well {well_id}')

# Graph aesthetics
plt.gca().invert_yaxis()
plt.xlabel('Temperature (°C)')
plt.ylabel('Depth (m)')
plt.title('Temperature Profile vs Depth for All Wells')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
