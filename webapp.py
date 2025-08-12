from flask import Flask, render_template, request, jsonify, redirect, url_for, make_response
import uuid
from Game import CrosswordGame

app = Flask(__name__)
app.secret_key = "dev-secret"  # für production ändern

# In-memory Speicher für Games (für Demo). Key: game_id (uuid)
GAMES = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    # words aus Textarea (newline/comma getrennt) oder default falls leer
    raw = request.form.get("words", "")
    mode = request.form.get("mode", "easy")

    words = [w.strip().lower() for w in raw.replace(",", "\n").splitlines() if w.strip()]
    if not words:
        # Default-Wortliste
        words = ["apple", "pear", "banana", "kiwi", "melon"]

    game = CrosswordGame(size=10)
    game.set_mode(mode)
    game.setup(words)

    game_id = str(uuid.uuid4())
    GAMES[game_id] = game

    resp = make_response(redirect(url_for("game_view", game_id=game_id)))
    resp.set_cookie("game_id", game_id)
    return resp

@app.route("/game/<game_id>")
def game_view(game_id):
    game = GAMES.get(game_id)
    if not game:
        return redirect(url_for("index"))

    grid = game.builder.grid
    placed = sorted(game.word_placed)
    return render_template("game.html", grid=grid, placed=placed, game_id=game_id)

@app.route("/guess", methods=["POST"])
def guess():
    game_id = request.form.get("game_id")
    guess_word = request.form.get("guess", "").strip().lower()

    game = GAMES.get(game_id)
    if not game:
        return jsonify({"status": "error", "message": "Game not found"}), 404

    result = game.check_word(guess_word)
    positions = []
    if result == "correct":
        positions = game.get_word(guess_word)

    completed = game.completed()
    return jsonify({"status": "ok", "result": result, "positions": positions, "completed": completed})

if __name__ == "__main__":
    app.run(debug=True)