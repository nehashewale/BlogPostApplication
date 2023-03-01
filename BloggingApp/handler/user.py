from flask_restful import Resource
from validator.user import  validate_user_schema
from flask import request
from dao.user import get_user_by_username,create_user,get_all_users
from views.user import get_user_response,get_all_users_response




class User(Resource):
    def post(self):
        # getting body 
        body = request.json
        user = get_user_by_username(body["username"])
        if user != None:
            reponse = get_user_response(user)
            return reponse
        user = create_user(body["username"], body["name"])
        reponse = get_user_response(user)
        return reponse
    
    def get(self):      
        # getting params
        params = request.args.to_dict()
        username = params.get('username', None) 
        if username:
            user = get_user_by_username(username)
            if not user:
                return  {"message" : "user not found", "is_success": False}
            response = get_user_response(user)
            return { "user" : response, "is_success": True}
        users = get_all_users()
        response = get_all_users_response(users)
        return { "user_list" : response, "is_success": False}