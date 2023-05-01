
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 実行されるファイル(test_flask-migrate.py)の置き場所をbasedirに保存
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# データベースファイルは実行ファイルと同じ場所にapp.dbという名前で作成
app.config['SQLALCHEMY_DATABASE_URI'] \
    = 'mysql+pymysql://{user}:{password}@{host}/todo?charset=utf8' \
    .format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'host': os.getenv('DB_HOST', 'localhost'),
    })
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# migrateインスタンスを定義
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # この関数は、インタープリタ(コンソール)からこのクラス(からできたインスタンス)を読んだ際に、どのように表示されるかを定義している。ここではusernameを表示させている。
    def __repr__(self):
        return '<User {}>'.format(self.username)
