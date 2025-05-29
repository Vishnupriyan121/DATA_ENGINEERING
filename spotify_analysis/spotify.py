from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector
#set up Client Credentials
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='d5b0b3579b6c4924800a535e329e385f',
    client_secret='265ffd40e0e342c78d76a9e6a9df64a5'
))

#database configuration

db_config={
    'host': 'localhost',
    'database': 'test',
    'user': 'root',
    'password': 'IFET@2022',
}

# Connect to the database
connection=mysql.connector.connect(**db_config)
cursor=connection.cursor()

file_path="track_url_link.txt"
with open(file_path,'r') as file:
    track_urls=file.readlines()

for track_url in track_urls:
    track_url=track_url.strip()

    try:

        track_id=re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

        track=sp.track(track_id)
        print(track)

        track_data={
            'Track Name':track['name'],
            'Artist':track['artists'][0]['name'],
            'Album':track['album']['name'],
            'Popularity':track['popularity'],
            'Duration(minutes)':track['duration_ms']/6000
        }
        insert_query="""
        INSERT INTO spotify_tracks(track_name,artist,album,popularity,duration_minutes)
        VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_query,(
            track_data['Track Name'],
            track_data['Artist'],
            track_data['Album'],
            track_data['Popularity'],
            track_data['Duration(minutes)']
        ))
        connection.commit()

        print(f"Inserted:{track_data['Track_Name']} by {track_data['Artist']}")
    except Exception as e:
        print(f"Error occured:{track_url},Error:{e}")

print(f"\nTrack Name: {track_data['Track Name']}\n")
print(f"Artist:{track_data['Artist']}\n")
print(f"Album:{track_data['Album']}\n")
print(f"Popularity:{track_data['Popularity']}\n")
print(f"Duration:{track_data['Duration(minutes)']:.2f}minutes")

df=pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

df.to_csv('spotify_track_data.csv',index=False)

features=['Popularity','Duration(minutes)']
values=[track_data['Popularity'],track_data['Duration(minutes)']]

plt.figure(figsize=(8,5))
plt.bar(features,values,color='skyblue',edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}")
plt.ylabel('Value')
plt.show()
cursor.close()
connection.close()
