from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable

app = Flask(__name__)

@app.route('/youtube_transcript_api', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({"error": "video_id manquant"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'fr'])
        return jsonify(transcript), 200
    except TranscriptsDisabled:
        return jsonify({"error": "Les sous-titres sont désactivés pour cette vidéo"}), 404
    except VideoUnavailable:
        return jsonify({"error": "Vidéo introuvable ou indisponible"}), 404
    except Exception as e:
        # Loggez l'erreur pour la voir dans les logs Render
        app.logger.error(e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
