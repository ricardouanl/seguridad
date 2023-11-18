from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_balances = {
    'Cliente1': 1000,
    'Cliente2': 1000
}

@app.route('/')
def index():
    return render_template('index.html', user_balances=user_balances, token='123')

@app.route('/transfer', methods=['POST'])
def transfer():
    token = request.form.get('token', '')
    #if token == '123':
    user_id = request.form.get('user_id', '')
    amount = int(request.form.get('amount', 0))
    user_balances[user_id] -= amount
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

