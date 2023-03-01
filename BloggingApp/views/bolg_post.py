def get_blogs_reponse(blogs):
    response_blogs = []
    for blog in blogs:
        response_blogs.append(
            {
            "uuid" : blog.uuid,
            "user_name" : blog.user.username,
            "content" : blog.content,
            "like_count" : blog.likes.count(),
            "is_private" : True if blog.access_type == "PRIVATE" else False
            }
        )
    return response_blogs