import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Group by 'machine_id' and calculate the sum of NaNs in 'ride_cost'
df['feature_nans'] = df.groupby('machine_id')['ride_cost'].transform(lambda x: x.isna().sum())

# Save the updated dataset
df.to_csv('your_dataset_with_feature_nans.csv', index=False)
