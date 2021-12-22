from passlib.context import CryptContext


# API Tokens are hashed in the DB and should at no point ever be read as plain text.
token_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)


def hash_token(token):
    return token_context.hash(token)


def check_hashed_token(token, hashed):
    return token_context.verify(token, hashed)


from .DbConn import DbConnection
from .PgConn import PgConnection

