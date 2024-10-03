from flask import Flask, render_template, request, jsonify
from app.services.rag_service import RAGService

app = Flask(__name__)
rag_service = RAGService()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    user_query = request.json["query"]
    response = rag_service.query(user_query)
    return jsonify({"response": response})


@app.route("/update_note", methods=["POST"])
def update_note():
    note_path = request.json["note_path"]
    new_content = request.json["new_content"]
    rag_service.update_note(note_path, new_content)
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
