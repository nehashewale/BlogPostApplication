from flask import Flask
from flask_restful import Resource, Api
from handler.ping import Ping,Index
from handler.user import User
from handler.bolg_post import Blog
from handler.blog_like import Like
app = Flask(__name__)
api = Api(app)
api.add_resource(Index, '/')
api.add_resource(Ping, '/ping/')
api.add_resource(User, '/user/','/user/<string:username>/')
api.add_resource(Blog,'/blog/')
api.add_resource(Like,'/like/')


if __name__ == '__main__':
    app.run(debug=True, port=5000)