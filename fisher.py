from flask import Flask,make_response
app=Flask(__name__)
app.config.from_object('config')


@app.route("/book/search/<q>/<page>")
def search(q,page):
    """
    q,普通关键字和isbn
    page
    :return:
    """
    isbn_or_key="key"
    if len(q)==13 and q.isdigit():
        isbn_or_key="isbn"
    short_q=q.replace("-","")
    if "-" in q and len(short_q)==10 and short_q.isdigit():
        isbn_or_key="isbn"
    pass

# app.add_url_rule('/hello',view_func=hello)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=88)