from flask import Flask
from routes import data_bp
from errors import register_error_handlers

app = Flask(__name__)

# blueprints
app.register_blueprint(data_bp)

# error handlers
register_error_handlers(app)

if __name__ == '__main__':
    app.run(debug=True)
