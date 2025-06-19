# add_2_yt_playlist

**Description:**  
This program allows you to take a list of songs, search YouTube for the first result, and add it to your playlist. You can use this tool to migrate from Spotify or another platform, or as a building block for your own playlist automation.

**Disclaimer:**  
This tool is limited to adding up to 100 songs per day unless you increase your YouTube API quota to over 10,000 units per day. Each search consumes 100 units. More details on API quota can be found here: [YouTube API Quotas](https://developers.google.com/youtube/v3/determine_quota_cost).

## Step 1: Create OAuth Credentials

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project (if you haven't already).
3. Enable the **YouTube Data API v3**.
4. Navigate to **APIs & Services > Credentials**.
5. Click **Create Credentials** and select **OAuth 2.0 Client ID**.
6. Set up the OAuth consent screen if prompted.
7. Select **Desktop App** as the application type.
8. After creating the credentials, click **Download** to get your credentials file.
9. Rename the file to `credentials.json` and place it in your project directory.
10. Add your email as a test user under the newly created API key.

## Step 2: Replace Playlist ID

1. Navigate to your playlist in YouTube.
2. Find the playlist ID in the URL (e.g., `playlist?list=PLAYLIST_ID`).
3. Replace the `PLAYLIST_ID` in the script with your own playlist ID.
