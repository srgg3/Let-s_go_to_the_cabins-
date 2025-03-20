from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    astronauts = [
        "Капитан Джон Смит",
        "Астронавт Алан Бин",
        "Астронавт Нил Армстронг",
        "Астронавт Юрий Гагарин",
        "Астронавт Валентина Терешкова"
    ]
    return render_template('distribution.html', astronauts=astronauts)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')