

class UserService:

    def get_all_users(self):
        # Dummy data - In real scenario, fetch from database
        users = [
            {'id': 1, 'name': 'Alice', 'email': 'pk@gmail.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@gmail.com'},
        ]
        return users