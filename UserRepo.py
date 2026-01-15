class UserRepo:
    def __init__(self, user_list: UserService):
        self.user_list = user_list

    def get_user_by_id(self, user_id):
        return self.user_list.get_all_users().filter(id == user_id).first()

    def get_all_users(self):
        return self.user_list.get_all_users()
    
    def add_user(self, user):
        self.user_list.get_all_users().append(user)

    def delete_user(self, user):
        self.user_list.get_all_users().remove(user)