from flask import Blueprint, render_template, request, redirect
from app.utils.parser import parse_sop_file
from app.models.embedding_model import add_document
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/chat')
def chat():
    return render_template('chat.html')

@main_bp.route('/upload_sop', methods=['GET', 'POST'])
def upload_sop():
    if request.method == 'POST':
        file = request.files['sop_file']
        if file:
            path = os.path.join('sop_docs', file.filename)
            file.save(path)
            text = parse_sop_file(path)
            add_document(text, f"{file.filename} - embedded")
            return redirect('/upload_sop')
    return render_template('sop_upload.html')
