import os

from dotenv import load_dotenv

from . import create_app

load_dotenv()

app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/')
def hello():
      return "Hello World!"

if __name__ == "__main__":
      app.run()