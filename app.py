import random

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "mock_demo_secret_key"

WORDS = [
    "river",
    "mountain",
    "sun",
    "moon",
    "spaceship",
    "bird",
    "spider",
    "car",
    "train",
]


def mock_ai_guess(description):
    return random.choice(WORDS)


@app.route("/")
def index():
    session.clear()
    session["score"] = 0
    session["correct"] = 0
    session["incorrect"] = 0
    session["skipped"] = 0
    session["used_words"] = []
    return redirect(url_for("game"))


@app.route("/game")
def game():
    if len(session.get("used_words", [])) == len(WORDS):
        return redirect(url_for("results"))

    remaining_words = list(set(WORDS) - set(session["used_words"]))
    current_word = random.choice(remaining_words)
    session["current_word"] = current_word
    session["used_words"].append(current_word)

    return render_template(
        "game.html",
        word=current_word,
        correct=session["correct"],
        incorrect=session["incorrect"],
        skipped=session["skipped"],
    )


@app.route("/submit_description", methods=["POST"])
def submit_description():
    data = request.get_json()
    description = data.get("description", "")
    actual_word = session.get("current_word", "")
    ai_guess = mock_ai_guess(description)

    correct = ai_guess.lower() == actual_word.lower()
    if correct:
        session["score"] += 100
        session["correct"] += 1
    else:
        session["incorrect"] += 1

    return jsonify(
        {
            "ai_guess": ai_guess,
            "score": session["score"],
            "correct": session["correct"],
            "incorrect": session["incorrect"],
            "skipped": session["skipped"],
        }
    )


@app.route("/skip", methods=["POST"])
def skip():
    session["skipped"] += 1
    return jsonify(
        {
            "skipped": session["skipped"],
            "correct": session["correct"],
            "incorrect": session["incorrect"],
            "score": session["score"],
        }
    )


@app.route("/next_word")
def next_word():
    if len(session.get("used_words", [])) == len(WORDS):
        return jsonify({"word": None})  # Game over

    remaining_words = list(set(WORDS) - set(session["used_words"]))
    current_word = random.choice(remaining_words)
    session["current_word"] = current_word
    session["used_words"].append(current_word)

    return jsonify({"word": current_word})


@app.route("/results")
def results():
    return jsonify(
        {
            "score": session.get("score", 0),
            "correct": session.get("correct", 0),
            "incorrect": session.get("incorrect", 0),
            "skipped": session.get("skipped", 0),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
