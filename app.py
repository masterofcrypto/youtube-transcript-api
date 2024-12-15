from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable

app = Flask(__name__)

@app.route('/youtube_transcript_api', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "Le paramètre 'video_id' est manquant"}), 400

    try:
        # Essaye d'obtenir les sous-titres en français, sinon en anglais
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
        return jsonify(transcript), 200
    except TranscriptsDisabled:
        return jsonify({"error": "Les sous-titres sont désactivés pour cette vidéo"}), 404
    except VideoUnavailable:
        return jsonify({"error": "Vidéo introuvable ou indisponible"}), 404
    except Exception as e:
        # Log l'erreur pour la voir dans les logs Render
        app.logger.error(f"Erreur lors de la récupération des sous-titres: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
