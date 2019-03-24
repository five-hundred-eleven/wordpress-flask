import bcrypt
from pythonwp.exceptions.InvalidPasswordException import InvalidPasswordException
from pythonwp.models.User import User
from pythonwp import db

class UserService:

    def __init__(self):
        pass

    def getUser(self, user_id, password):

        user = self.__getUser(user_id)
        if not self.__checkPassword(user, password):
            raise InvalidPasswordException()
        
        return user

    def __cryptPassword(self, password):
        '''
            Note that the password encryption in this module does not implement
            PHPass which wordpress uses. Therefore if you have wp_users created by
            wordpress you will need to update their passwords manually.
        '''

        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode("utf-8"), hash)
        return hash


    def __checkPassword(self, user, password):
        stored_hash = user.user_pass.encode("utf-8")
        password = password.encode("utf-8")
        return stored_hash == bcrypt.hashpw(password, stored_hash)


    def __getUser(self, user_id):

        return (
            User.query
                .filter(db.or_(
                    User.user_email==user_id,
                    User.user_login==user_id
                ))
                .one()
        )
