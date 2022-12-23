from abstract_repository  import AbstractRepository

class UserRepository(AbstractRepository):

    def __init__(self, session) -> None:

        self.session = session

    
    def get_all(self):
        # self.session.query(User).all()
        return ['jorge', 'Blanquicett', 'Matos']

    
    def get_by_id(self, id):
        ...

    
    def create(self, instance):
        ...

    
    def update(self, id):
        ...

    
    def delete(self, id):
        ...
