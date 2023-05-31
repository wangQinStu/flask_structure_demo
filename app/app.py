from flask import Flask
#1.创建config.py并导入和绑定
import config
#2.创建extension文件并导入db(解决循环引用的问题)
from exts import db
#3.创建ORM模型modules并导入
from models import UserModel
#4.导入并注册蓝图
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp


app = Flask(__name__)
#1.绑定配置文件
app.config.from_object(config)
#2.在app中绑定db
db.init_app(app)
#4.注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)



if __name__ == '__main__':
    app.run()
