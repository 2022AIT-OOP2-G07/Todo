from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/address
@app.route('/', methods=["GET"])
def todo_get():

    # パラメータの取得
    #yotei = request.args.get('schedule-input', None)
    #datetime = request.args.get('datetime-input', None)
    
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)



