from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/template')
def template():
    print(request.query_string)
    return render_template("index.jinja",name=request.args.get('name'))

if(__name__=="__main__"):
    app.run(debug=True)