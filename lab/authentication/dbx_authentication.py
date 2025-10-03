import dropbox
from lab.authentication.authentication import Authenticator
from lab.configuration.config import Config

class DBXAuthentication(Authenticator):
    def __init__(self):
        pass

    def get_access_token(self):
        dbx = dropbox.Dropbox(Config.DROPBOX_ACCESS_TOKEN)
        try:
            dbx.users_get_current_account()
            print("Authentication successful!")
        except Exception as e:
            print("Error authenticating:", e)
            return None
        return dbx
