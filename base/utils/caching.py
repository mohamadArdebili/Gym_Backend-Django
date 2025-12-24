from django.core.cache import cache
from base.utils.constants import Constant
from Crypto.Random.random import randint


class CachingProcedureHandler:
    """ setting and getting data from cache """

    def __init__(self):
        # otp_code range, using Values stored in Constant class
        self.token_from = Constant.RANDOM_TOKEN_FROM
        self.token_to = Constant.RANDOM_TOKEN_TO
        self.expiration = Constant.REDIS_EXPIRATION

    def set_key(self, type, email, token):
        """ store a single key, in cache """
        # cache.set("name": "Ali", 5)
        return cache.set(f"{type} : {token}", email, self.expiration)

    def get_key(self, type, token):
        """ get a key from cache """
        return cache.get(f"{type} : {token}")

    def generate_token(self):
        """ generate a random token """
        token = randint(int(self.token_from), int(self.token_to))
        return str(token)
