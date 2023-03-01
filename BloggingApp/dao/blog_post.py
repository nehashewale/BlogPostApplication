import django;django.setup()
import uuid

from BloggingApp.blogdata.models import Post,User,Like

# user dao
def get_user_by_username(user_name):
    try:
        user = User.objects.get(username=user_name)
    except:
        user = None
    return user

def create_blog_or_post(user, content, is_private):
    access_type = Post.PRIVATE if is_private else Post.PUBLIC
    post = Post.objects.create(
        uuid = uuid.uuid4().hex,
        user=user,
        content=content,
        access_type=access_type
    )
    return post

def get_blog_by_user_and_uuid(uuid,username):
    try:
        blog = Post.objects.get(uuid=uuid,user__username= username)
    except:
        blog = None
    return blog

def archive_blog(blog):
    archived  = False
    try:
        blog.archived = True
        blog.save()
        archived = True
    except:
        pass
    return archived


def get_all_blogs_by_userid(user_id):
    blogs = Post.objects.filter(user_id=user_id)
    return blogs    


def get_all_public_blogs():
    blogs = Post.objects.filter(access_type=Post.PUBLIC)
    return blogs  



def get_blog_by_uuid(uuid):
    try:
        blog = Post.objects.get(uuid=uuid)
    except:
        blog = None
    return blog


def check_if_blog_alredy_liked_by_user(blog_uuid, username):
    likes = Like.objects.filter(post_uuid=blog_uuid,user__username=username)
    if likes.count() > 0:
        return True
    return False

def associate_like(blog, user):
    like = Like.objects.create(
        user =user,
        post_uuid=blog.uuid
    )
    blog.likes.add(like)
    blog.save()