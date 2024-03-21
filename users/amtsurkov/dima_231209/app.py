from flask import Flask
from redis import Redis
from flask import render_template
from flask import request, url_for, flash, redirect

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)

@app.route('/', methods=('GET', 'POST'))
def hello():
    #redis.incr('hits')
    #return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    #return "<html><form>Давай поговорим:<br><textarea rows='10' cols='45' name='question'></textarea><br><input type='button' value='Отправить'></form></html>"
    posts = [
                {
                    'title': 'мой вопрос'
                },
                {
                    'title': 'ответ сети'
                }
            ]

    question = ''
    if request.method == 'POST':
        question = request.form['question']

    posts[1]['title'] += ' на вопрос ' + question
    return render_template('index.html', posts=[ posts[1]])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
