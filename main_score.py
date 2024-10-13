from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
        return render_template_string('<h1>Score: {{score}}</h1>', score=score)
    except Exception as e:
        return render_template_string("<h1>Error</h1>")

if __name__ == '__main__':
    app.run(debug=True)
