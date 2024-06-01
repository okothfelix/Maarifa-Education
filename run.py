from flask import Flask
from flask_cors import CORS
from frontend.routes import frontend_bp
from marketplace.routes import marketplace_bp

app = Flask(__name__)
app.secret_key = '70b76438bbccfd3ec8ab0ec170d4e179'
CORS(app, resources={r'*': {'origins': 'https://maarifaedu.co.ke'}})

app.register_blueprint(frontend_bp, url_prefix='/')
app.register_blueprint(marketplace_bp, url_prefix='/marketplace')

if __name__ == '__main__':
    app.run(debug=True)
