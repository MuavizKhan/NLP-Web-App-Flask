import json
import os


class Database:
    def __init__(self):
        self.db_path = 'users.json'
        # Crucial Cloud Fix: Initialize the file immediately if it doesn't exist
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump({}, f)

    def insert(self, name, email, password):
        # Read current state safely
        with open(self.db_path, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}

        if email in users:
            return False  # Already exists

        # Add new user object
        users[email] = {
            'name': name,
            'password': password
        }

        # Write back to disk
        with open(self.db_path, 'w') as f:
            json.dump(users, f, indent=4)
        return True

    def search(self, email, password):
        with open(self.db_path, 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                return False

        if email in users:
            if users[email]['password'] == password:
                return True
        return False