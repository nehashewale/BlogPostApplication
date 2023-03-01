from flask_restful import Resource
from flask import request
from views.bolg_post import get_blogs_reponse
from dao.blog_post import get_user_by_username, create_blog_or_post,get_all_blogs_by_userid,get_blog_by_user_and_uuid,get_all_public_blogs,archive_blog
class Blog(Resource):
    def post(self):
        # getting body 
        body = request.json

        # validate body

        # check user 
        user = get_user_by_username(body["username"])
        if not user:
            return {"message" : "usernot found", "is_success": False}
        #  create Blog
        blog = create_blog_or_post(user, body["content"], body["is_private"])
        
        if not blog:
            return { "is_success": False}
        return { "blog_uuid" : blog.uuid, "is_success": True}
    
    def get(self):      
        # getting params
        params = request.args.to_dict()
        username = params.get('username', None) 
        if username:
            user = get_user_by_username(username)
            if not user:
                return  {"message" : "usernot found", "is_success": False}
            blogs = get_all_blogs_by_userid(user.id)
        else:
            blogs = get_all_public_blogs()
        blog_list = get_blogs_reponse(blogs)
        return { "blog_list" : blog_list, "is_success": True}

    def delete(self):
        # getting body 
        body = request.json
        blog = get_blog_by_user_and_uuid(body["uuid"], body["username"])
    
        if not blog:
           
            return { "is_success": False}
        is_archived = archive_blog(blog)
        
        return  { "is_success": is_archived}
    
    


