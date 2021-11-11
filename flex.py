from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", title="Main", menu=menu)
@app.route("/about")
def about():
    return render_template("test.html", title="О сайте", menu=menu)
menu = ["Установка","Первое приложение","Обратная связь"]
if __name__=="__main__":
    app.run(debug=True)