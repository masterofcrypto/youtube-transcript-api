from youtube_transcript_api import YouTubeTranscriptApi

# Remplacez l'URL ci-dessous par celle de la vidéo YouTube dont vous voulez la transcription
video_url = "https://www.youtube.com/watch?v=9UIETO3bcsc"

# Extraction de l'ID de la vidéo
video_id = video_url.replace("https://www.youtube.com/watch?v=", "")

try:
    # Récupération de la transcription (par défaut en anglais)
    transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

    # Conversion en texte brut
    text_content = "\n".join(segment['text'] for segment in transcript_data)

    # Affichage dans les logs (visible dans l'onglet "Logs" sur Render)
    print("Transcription :")
    print(text_content)

except Exception as e:
    # En cas d'erreur (par exemple si la transcription n’est pas disponible)
    print("Erreur lors de la récupération de la transcription :", e)
