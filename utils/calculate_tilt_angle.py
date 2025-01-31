import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Define a function to calculate the tilt angle
def calculate_tilt_angle(series):
    # Assuming tilt angle is calculated as the arctan of the mean user ride quality
    return np.degrees(np.arctan(series.mean()))

# Group by 'machine_id' and calculate the tilt angle based on 'user_ride_quality'
df['feature_corner'] = df.groupby('machine_id')['user_ride_quality'].transform(calculate_tilt_angle)

# Save the updated dataset
df.to_csv('your_dataset_with_feature_corner.csv', index=False)
