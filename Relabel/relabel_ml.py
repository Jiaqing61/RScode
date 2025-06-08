# Apply Kamiran & Calders Data Re-labeling on ml-1m dataset (RecBole style)
import pandas as pd

# Load data files
user_df = pd.read_csv('dataset/ml-1m/ml-1m.user', sep='\t')
inter_df = pd.read_csv('dataset/ml-1m/ml-1m.inter', sep='\t')

# Merge to associate gender with interactions
data = pd.merge(inter_df, user_df, on='user_id:token')

# Define binary label: rating ≥ 4 → positive (1), else 0
data['label'] = (data['rating'] >= 4).astype(int)

# Keep only necessary columns
data = data[['user_id', 'item_id', 'label', 'rating', 'timestamp', 'gender']]

# Compute target (minimum) positive rate across groups
group_stats = data.groupby('gender')['label'].mean()
target_rate_min = group_stats.min()

# Compute global target rate
target_rate_global = data['label'].mean()  # Global average (demographic parity goal)
def relabel_group_ranked(df, gender_value, target_rate):
    group_df = df[df['gender'] == gender_value].copy()
    current_rate = group_df['label'].mean()

    if current_rate <= target_rate:
        return df  # No relabeling needed

    # Number of positive labels to flip
    excess_positives = int((current_rate - target_rate) * len(group_df))

    # Sort positive instances by rating (lowest first)
    candidates_to_flip = group_df[group_df['label'] == 1].sort_values(by='rating')

    # Get indices to flip
    flip_indices = candidates_to_flip.head(excess_positives).index

    # Apply flip
    df.loc[flip_indices, 'label'] = 0
    return df

# Apply relabeling for both groups
data = relabel_group_ranked(data, 'M', target_rate_min)
data = relabel_group_ranked(data, 'F', target_rate_min)

# Drop gender column (optional for fairness-unaware training)
data.drop(columns=['gender'], inplace=True)

# Rename 'label' back to 'rating' for RecBole compatibility (binary relevance)
data.rename(columns={'label': 'rating'}, inplace=True)

# Save the relabeled interaction file
data[['user_id', 'item_id', 'rating', 'timestamp']].to_csv(
    'dataset/ml-1m/ml-1m.inter', sep='\t', index=False
)

print("✅ Ranked re-labeling complete. New 'ml-1m.inter' file ready for RecBole.")
