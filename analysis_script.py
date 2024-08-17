import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Load the CSV file into a DataFrame
df = pd.read_csv('top_videos.csv')

# Group by channel and sum the view counts
channel_views = df.groupby('Channel')['Views'].sum().reset_index()

# Sort by view counts
channel_views = channel_views.sort_values(by='Views', ascending=False)

# Set the figure size and style
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Create a bar plot of view counts by channel
sns.barplot(x='Views', y='Channel', data=channel_views)

# Set plot title and labels
plt.title('Total Views by Channel')
plt.xlabel('Total Views')
plt.ylabel('Channel')

# Adjust y-axis labels to ensure full names are visible
plt.gca().margins(y=0.1)  # Add some margin to the y-axis

# Format x-axis labels to show numbers in thousands (k)
formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x/1000)}k')
plt.gca().xaxis.set_major_formatter(formatter)

# Show the plot and save it
plt.savefig('views_by_channel.png')
plt.show()
