
# 🎵 Spotify Track Metadata ETL Project

This project extracts metadata of Spotify tracks using the Spotify Web API via the `spotipy` library, transforms it, and loads it into a MySQL database. It also visualizes track popularity and duration using Matplotlib.

---

## 📌 Features

- ✅ Extracts track data from a list of Spotify track URLs  
- ✅ Parses metadata like Track Name, Artist, Album, Popularity, and Duration  
- ✅ Stores the data into a MySQL database table  
- ✅ Converts data into a Pandas DataFrame and saves it as a CSV  
- ✅ Plots a bar chart of track popularity and duration

---

## 🛠️ Technologies Used

- **Python**
- **Spotify Web API** (via `spotipy`)
- **MySQL**
- **Pandas**
- **Matplotlib**
- **Regex**


---

## 📝 Prerequisites

- Python 3.x
- MySQL Server running with a database created
- A valid Spotify Developer account to get `client_id` and `client_secret`

---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/spotify-track-etl.git
   cd spotify-track-etl

2. Install dependencies

pip install spotipy pandas matplotlib mysql-connector-python


3. Update configuration

In spotify.py, replace:

client_id and client_secret with your Spotify credentials

MySQL host, user, password, and database values




4. Prepare database Create the table spotify_tracks:

CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);


5. Add track URLs

Edit the track_url_link.txt file and add one Spotify track URL per line



6. Run the script

python spotify.py




---

📊 Output

Data is inserted into the MySQL table spotify_tracks

A CSV file spotify_track_data.csv is generated

A bar chart is displayed showing:

Track popularity

Duration in minutes




---

📌 Example

Input (from track_url_link.txt):

https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp

Console Output:

Inserted: Hey Ya! by OutKast

Track Name: Hey Ya!
Artist: OutKast
Album: Speakerboxxx/The Love Below
Popularity: 80
Duration: 3.55 minutes


---

🚀 Future Improvements

Add support for batch processing and multiple track visualizations

Use .env file to secure credentials

Add exception logging to a log file

Deploy with a simple Flask front-end


