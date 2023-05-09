from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/movie_db"
SQLALCHEMY_TRACK_MODIFICATIONS = True


from extensions import *
from controllers import *
from models import *

if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=5000, debug=True)