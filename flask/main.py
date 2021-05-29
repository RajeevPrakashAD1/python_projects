from flask import Flask
app = Flask(__name__)
import random

num = random.randint(1,10)

@app.route('/')
def hello_world():
    return '<h1> Guess a Number Between 0 and 9</h1> ' \
           '<img src="https://media2.giphy.com/media/Kehzyp9EFa2IYDte8P/200w.webp?cid=ecf05e47c7femaje4e7y4w8lcggpdrwrkf034x0hvct212jc&rid=200w.webp">'


@app.route('/bye')
def bye():
    return "bye"

@app.route('/<int:number>')
def check(number):
    if number>num:
        return '<h1> WRONG its bigger</h1>' \
               '<img src="https://media3.giphy.com/media/HDeItv0iSeN0c/200.webp?cid=ecf05e475v2w7xokhrydo71bowc5qdsw4n87kryl4qkvrukf&rid=200.webp">'
    elif number < num:
        return '<h1> Wrong its smaller </h1>' \
               '<img src="https://media2.giphy.com/media/M9Isn1h9cy3hBD3DUN/200w.webp?cid=ecf05e47x1ag35mdo0vsc1d9rf9h9wwsw1bends6sdpbabd5&rid=200w.webp">'
    else:
        return '<h1> RIGHT you found </h1>' \
               '<imf src="https://media4.giphy.com/media/3oz8xAFtqoOUUrsh7W/200w.webp?cid=ecf05e47bq87kwkh4eidxvgpf00u275j6wk4ut6uz7xuf84x&rid=200w.webp">'



if __name__ == '__main__':
    app.run(debug=True)
