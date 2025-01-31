import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Group by 'machine_id' and get the first value of 'deviation_normal' for each group
df['feature_start'] = df.groupby('machine_id')['deviation_normal'].transform('first')

# Save the updated dataset
df.to_csv('your_dataset_with_feature_start.csv', index=False)
