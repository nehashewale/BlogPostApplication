from flask_restful import Resource
from flask import request
from dao.blog_post import get_blog_by_uuid, check_if_blog_alredy_liked_by_user,associate_like
from dao.user import get_user_by_username
class Like(Resource):
    def post(self):
        # getting body 
        body = request.json

        # validate body

        # check user 
        user = get_user_by_username(body["username"])
        if not user:
            return {"message" : "usernot found", "is_success": False}
        #get blog 
        blog = get_blog_by_uuid(body["blog_uuid"])
        if not blog:
            return {"message" : "blog found", "is_success": False}
        is_already_liked = check_if_blog_alredy_liked_by_user(body["blog_uuid"],body["username"])
        if is_already_liked:
            return {"message" : "already liked by user", "is_success": False}
        associate_like(blog, user)
        return { "message" : "blog liked", "is_success": True}