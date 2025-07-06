from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Render will inject PORT into environment (use default 10000 locally)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
