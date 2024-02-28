from main import initialise_objects, create_user, user_list

initialise_objects()

print(user_list)

for user in user_list:
    print(user.get_username())

