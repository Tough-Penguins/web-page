from _app import app

@app.errorhandler(404)
def page_not_found(e):
    """Método para manejar los errores de tipo 404."""
    return "404 D:"

@app.route('/', methods=['GET'])
def index():
    return "Bienvenido :D"

if __name__ == '__main__':
    app.debug = True
    app.run()
