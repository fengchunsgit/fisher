from flask import Flask,make_response
app=Flask(__name__)
app.config.from_object('config')


@app.route("/book/search")
def search():
    """
    q,普通关键字和isbn
    page
    :return:
    """
    pass

# app.add_url_rule('/hello',view_func=hello)
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=88)