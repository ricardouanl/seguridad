from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('b/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

