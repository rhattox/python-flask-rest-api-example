from flask import Flask
from .routes.home import home
from .routes.user import user
import logging

app = Flask(__name__)

# Enable Logging
app.logger.setLevel(logging.DEBUG)

# Routes
app.register_blueprint(home)
app.register_blueprint(user)

if __name__ == "__main__":
    app.run(debug=True)