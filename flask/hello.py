from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello World"
    return name


@app.route('/good')
def good():
    name = "Good"
    return name


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/confirm', methods=['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template("confirm.html", result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
