from youtube_transcript_api import YouTubeTranscriptApi

# URL complète de la vidéo YouTube
video_url = "https://www.youtube.com/watch?v=9UIETO3bcsc"

# Extraire l'ID de la vidéo à partir de l'URL
video_id = video_url.replace("https://www.youtube.com/watch?v=", "")

# Récupérer la transcription (par défaut en anglais si disponible)
transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

# Convertir la liste de segments en texte brut
text_content = "\n".join(segment['text'] for segment in transcript_data)

# Afficher la transcription
print("Transcription :")
print(text_content)
