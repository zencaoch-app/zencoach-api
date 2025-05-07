from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/zencoach-prompt', methods=['POST'])
def recevoir_idee_video():
    data = request.json

    titre = data.get("titre")
    format_video = data.get("format")
    resume = data.get("resume")

    print(f"🎬 Nouvelle idée reçue : {titre} | Format : {format_video}")
    print(f"Résumé : {resume}")

    return jsonify({
        "status": "OK",
        "message": "Idée reçue. Prête pour génération de scène ou prompt."
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
