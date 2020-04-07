from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_word():
    return 'Hello world'


# @app.route('/name/<name>')
# def hello_name(name):
#     return "hello {}".format(name)


# 只接受int型参数 float只接受浮点型，默认是字符串 path接受用作目录分隔符的斜杠
@app.route('/<path:url_path>/')
def hello_name(url_path):
    return "hello {}".format(url_path)


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)
