
def get_user_response(user):
    user_response = {
        "username" : user.username,
        "name": user.name
    }
    return user_response


def get_all_users_response(users):
    users_response = []
    for user in users:
        user_response = get_user_response(user)
        users_response.append(user_response)
    return users_response


