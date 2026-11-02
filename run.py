import os
import webbrowser
from threading import Timer
from app import app

if __name__ == '__main__':
    # Abre o navegador automaticamente assim que o servidor arranca
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
        Timer(0.8, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
    app.run(debug=True)

