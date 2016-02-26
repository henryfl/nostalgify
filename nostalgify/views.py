from nostalgify import app

@app.route('/')
def index():
    return "main view"
