import django;django.setup()
import uuid

from BloggingApp.blogdata.models import User



def create_user(user_name,name):
    user = User.objects.create(
        username = user_name,
        name = name
        )
    return user

def get_user_by_username(user_name):
    try:
        user = User.objects.get(username=user_name)
    except:
        user = None
    return user


# dao user
def get_all_users():
    users = User.objects.all()
    return users

# view user


