import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Scopes for accessing YouTube data
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# The playlist ID of the playlist you want to add videos to
PLAYLIST_ID = 'REPLACE_ME'

# List of songs to search for and add to your playlist
songs_to_add = [
    "Crazy Train Ozzy Osbourne",
    "You Give Love A Bad Name Bon Jovi",
    "Still Just a Rat in a Cage Blue Light Special"
]

def authenticate_youtube():
    """Authenticate and create a YouTube API client."""
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube

def search_video(youtube, song_query):
    """Search for a video on YouTube based on a song query."""
    request = youtube.search().list(
        part="snippet",
        q=song_query,
        type="video",
        maxResults=1  # Get the first search result
    )
    response = request.execute()

    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        print(f"Found video for '{song_query}': https://www.youtube.com/watch?v={video_id}")
        return video_id
    else:
        print(f"No video found for '{song_query}'")
        return None

def add_video_to_playlist(youtube, video_id, playlist_id):
    """Add a video to a playlist."""
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )
    response = request.execute()
    print(f"Added video {video_id} to playlist {playlist_id}")

def main():
    youtube = authenticate_youtube()

    for song in songs_to_add:
        video_id = search_video(youtube, song)
        if video_id:
            add_video_to_playlist(youtube, video_id, PLAYLIST_ID)
            time.sleep(1)  # Wait for 1 seconds before adding the next video
if __name__ == "__main__":
    main()
