from flask_restful import Resource


class Ping(Resource):
    
    def get(self):
        return {"response" : "All OK"}
    
    
class Index(Resource):
    def get(self):
        return {"response" : "Server is running"}