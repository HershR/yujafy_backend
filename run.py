from flaskr import create_app
from config import *

if __name__ == "__main__":
    # app = create_app(config=config.TestingConfig)  # Dockerfile should use python run.py
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
