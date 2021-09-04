from _app import app
from flask.templating import render_template

@app.errorhandler(404)
def page_not_found(e):
    """Método para manejar los errores de tipo 404."""
    return render_template('404.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
