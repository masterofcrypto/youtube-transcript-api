from youtube_transcript_api import YouTubeTranscriptApi

video_url = "https://www.youtube.com/watch?v=2TL3DgIMY1g"
video_id = video_url.replace("https://www.youtube.com/watch?v=", "")

transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
text_content = "\n".join(segment['text'] for segment in transcript_data)

print("Transcription :")
print(text_content)
