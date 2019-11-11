from flask import Flask,make_response
app=Flask(__name__)
app.config.from_object('config')
from helper import is_isbn_or_key

@app.route("/book/search/<q>/<page>")
def search(q,page):
    isbn_or_key=is_isbn_or_key(q)
    pass

# app.add_url_rule('/hello',view_func=hello)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=88)