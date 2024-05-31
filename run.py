from flask import Flask
from flask_cors import CORS
from frontend.routes import frontend_bp

app = Flask(__name__, template_folder='frontend/templates')
app.secret_key = '70b76438bbccfd3ec8ab0ec170d4e179'
CORS(app, resources={r'*': {'origins': 'https://maarifaedu.co.ke'}})

app.register_blueprint(frontend_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
