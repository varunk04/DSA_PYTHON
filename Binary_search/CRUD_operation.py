"""
Problem-Statement:
--------------------------

As a backend engineer , you are tasked with developing a fast in-memory data structure to manage profile
information (username, name and email) for 100 million users. It should allow the following operations to be
performed efficiently:

    1. Insert the profile information for a new user.
    2. Find the profile information of a user, given their username
    3. Update the profile information of a user, given their username
    4. List all the users of the platform, sorted by username

You can assume that usernames are unique.
"""


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return 'user(username: {}, name : {}, email :{})'.format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


# Sample inputs and outputs:
varun = User('varun', 'varun foujdhar', 'varunf004@gmail.com')
varsha = User('varsha', 'varsha foudhar', 'varshaf004@gmail.com')
vadiraj = User('vadiraj', 'vadiraj foujdhar', 'vadirajf004@gmail.com')
rathna = User('rathna', 'rathna foujdhar', 'rathnaf004@gmail.com')

users = [varun, varsha, vadiraj, rathna]


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


# Creating the database
database = UserDatabase()

# Insering the data
database.insert(varun)
database.insert(varsha)
database.insert(vadiraj)
database.insert(rathna)
database.insert(User('sudhu', 'sudha bai', 'sudhaf@gmail.com'))

# FInding the user
user = database.find('varun')
print(user)

# Updating the user
database.update(User(username='varun', name='Varun Kumar Foujdhar', email='varunf004@gmail.com'))

# Finding all the users:
print(database.list_all())
