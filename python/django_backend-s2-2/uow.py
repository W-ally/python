from user_repository import UserRepository

class UserUOWPostgreSQL:
    ...

class UserUOWMongo:
    ...

class UserUOWSQLite:
    
    def __init__(self, session_factory):

        self.session = session_factory
        #.... handling de la session....
        self.user = UserRepository(self.session)#dependency injection

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()