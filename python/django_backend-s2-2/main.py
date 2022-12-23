from uow import UserUOWSQLite
from uow import UserUOWMongo

# uow = UserUOWSQLite('mongo://:akdajhhsdjjhdsjsdb:')
uow = UserUOWSQLite('sqlite://:memory:')

print(uow.user.get_all())