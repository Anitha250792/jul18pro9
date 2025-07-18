from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate_card():
    name = request.form.get('name')
    age = request.form.get('age')
    hobbies = request.form.get('hobbies').split(',')
    hobbies = [h.strip() for h in hobbies if h.strip()]
    return render_template('card.html', name=name, age=age, hobbies=hobbies)

if __name__ == '__main__':
    app.run(debug=True)
