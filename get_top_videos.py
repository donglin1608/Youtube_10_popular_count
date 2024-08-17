import requests
import csv

API_KEY = 'AIzaSyD5UAANejMpQb7imuuG3HigBi-dAct164M'  # Use the actual key or fetch from environment
URL = 'https://www.googleapis.com/youtube/v3/videos'
PARAMS = {
    'part': 'snippet,statistics',
    'chart': 'mostPopular',
    'maxResults': 10,
    'regionCode': 'US',
    'key': API_KEY
}

response = requests.get(URL, params=PARAMS)
data = response.json()

# Open a CSV file to write the data
with open('top_videos.csv', 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Channel', 'Views', 'Likes', 'Comments', 'Published At']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data['items']:
        writer.writerow({
            'Title': item['snippet']['title'],
            'Channel': item['snippet']['channelTitle'],
            'Views': item['statistics'].get('viewCount', 0),
            'Likes': item['statistics'].get('likeCount', 0),
            'Comments': item['statistics'].get('commentCount', 0),
            'Published At': item['snippet']['publishedAt']
        })

print("Top 10 most popular YouTube videos saved to top_videos.csv successfully!")
