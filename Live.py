from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/live')
def live():
    return "Application is live and running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
