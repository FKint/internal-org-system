from flask import Flask

app = Flask(__name__)
app.config.from_envvar('WEB_SETTINGS')


@app.route('/')
def view_home():
    return "Home page"


if __name__ == '__main__':
    app.run(debug=True, host=app.config['HOSTNAME'])
