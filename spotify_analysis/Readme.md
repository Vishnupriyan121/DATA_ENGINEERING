
# 🎵 Spotify Track Metadata ETL Project

This project extracts metadata of Spotify tracks using the Spotify Web API via the `spotipy` library, transforms it, and loads it into a MySQL database. It also visualizes track popularity and duration using Matplotlib.

---

## 📌 Features


# Spotify Track Metadata ETL

A compact ETL utility that extracts metadata for Spotify tracks using the Spotify Web API (via `spotipy`), transforms the data into a tabular format, loads it into a MySQL table, exports a CSV, and visualizes track popularity and duration.

---

## Features

- Read Spotify track URLs from `track_url_link.txt` (one URL per line)
- Fetch metadata: track name, artist, album, popularity, duration (minutes)
- Insert records into a MySQL table (`spotify_tracks`)
- Export results to `spotify_track_data.csv`
- Visualize popularity and duration with Matplotlib

---

## Prerequisites

- Python 3.8+
- A running MySQL server and a writable database
- Spotify Developer credentials (`SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`)

---

## Installation

From the project root, create a virtual environment and install dependencies (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install directly:

```powershell
pip install spotipy pandas matplotlib mysql-connector-python python-dotenv
```

`python-dotenv` is recommended to load credentials from a `.env` file.

---

## Configuration

Create a `.env` file in the project directory (recommended) with the following values:

```
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
MYSQL_HOST=localhost
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database
```

If `spotify.py` currently contains hard-coded credentials, switch it to read from environment variables (or use `python-dotenv`).

---

## Database setup

Run this SQL to create the target table:

```sql
CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
);
```

Ensure the configured MySQL user has INSERT privileges on the database.

---

## Usage

1. Add Spotify track URLs to `track_url_link.txt`, one per line. Example:

```
https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp
```

2. Run the script:

```powershell
python spotify.py
```

Outputs:
- New rows in `spotify_tracks` (MySQL)
- `spotify_track_data.csv` written in the project folder
- A Matplotlib bar chart showing popularity and duration

---

## Example output

Inserted: Hey Ya! by OutKast

Track Name: Hey Ya!  
Artist: OutKast  
Album: Speakerboxxx/The Love Below  
Popularity: 80  
Duration: 3.55 minutes

---

## Troubleshooting

- Authentication errors: confirm Spotify credentials and rate limits
- MySQL errors: verify host, user, password, database and network access
- Invalid URLs: ensure each line in `track_url_link.txt` is a Spotify track URL
- Headless plotting: replace `plt.show()` with `plt.savefig('plot.png')` when running on a server

---

## Improvements (suggested)

- Load credentials from `.env` via `python-dotenv` instead of hard-coding
- Add logging and retry logic for transient API/DB failures
- Batch and parallelize Spotify API requests for better throughput
- Add unit tests and CI to validate behavior
- Provide a lightweight Flask UI for uploading URL lists and viewing visualizations

---

## Files of interest

- `spotify.py` — main ETL script
- `track_url_link.txt` — input URLs (one per line)
- `spotify_track_data.csv` — generated CSV output

---

## License

MIT — adapt and reuse freely.


