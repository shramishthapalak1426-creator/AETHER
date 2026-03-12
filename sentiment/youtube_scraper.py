from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

API_KEY = "AIzaSyDwE4CeYm8xVGVHl_vTIDX8WyeWWYuNqfY"


def get_video_id(url):

    parsed = urlparse(url)

    if parsed.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed.query)["v"][0]

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    return None


def get_youtube_comments(url):

    video_id = get_video_id(url)

    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=50,
        textFormat="plainText"
    )

    response = request.execute()

    comments = []

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments
