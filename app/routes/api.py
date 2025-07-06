from flask import Blueprint, request, jsonify
from app.models.embedding_model import query_similar
from app.models.embedding_model import get_openai_response

api_bp = Blueprint('api', __name__)

@api_bp.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get("question")
    mode = data.get("mode", "offline")
    context = "\n".join(query_similar(query))

    if mode == "online":
        answer = get_openai_response(query, context)
    else:
        answer = context
    return jsonify({"response": answer})
