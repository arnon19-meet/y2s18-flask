from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    pets=["dragging dragon", "katrin cat" ]
    return render_template(
        "index.html",
        pets=pets
    )


if __name__ == '__main__':
   app.run(debug = True)