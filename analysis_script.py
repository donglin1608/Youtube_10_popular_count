import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('top_videos.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Basic statistics on the view counts
print(df['Views'].describe())

# Group by channel and sum the view counts
channel_views = df.groupby('Channel')['Views'].sum().reset_index()

# Sort by view counts
channel_views = channel_views.sort_values(by='Views', ascending=False)

# Display the sorted data
print(channel_views)

# Set the figure size and style
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")

# Create a bar plot of view counts by channel
sns.barplot(x='Views', y='Channel', data=channel_views)

# Set plot title and labels
plt.title('Total Views by Channel')
plt.xlabel('Total Views')
plt.ylabel('Channel')

# Show the plot
plt.show()

plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
sns.barplot(x='Views', y='Channel', data=channel_views)
plt.title('Total Views by Channel')
plt.xlabel('Total Views')
plt.ylabel('Channel')
plt.savefig('views_by_channel.png')  # Save the plot as a PNG file
plt.show()
