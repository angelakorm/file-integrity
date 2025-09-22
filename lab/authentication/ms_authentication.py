from lab.authentication.authentication import Authenticator
from msal import PublicClientApplication
from lab.configuration.config import Config

class MSAuthentication(Authenticator):
    def __init__(self):
        self.app = PublicClientApplication(client_id=Config.CLIENT_ID, authority=Config.AUTHORITY)

    def get_access_token(self):
        result = None
        accounts = self.app.get_accounts()

        if accounts:
            chosen = accounts[0]
            result = self.app.acquire_token_silent([Config.SCOPES], account=chosen)
            print("Silent authentication.")

        if not result:
            print("No suitable token in cache found, getting a new one from Azure AD.")
            result = self.app.acquire_token_interactive(scopes=[Config.SCOPES], prompt="select_account")

        if "access_token" in result:
            print("Authentication success. This is your token: ")
            print(result["access_token"])
            return result["access_token"]
        else:
            print(result.get("error"))
            print(result.get("error_description"))
            print(result.get("correlation_id"))
            raise Exception("Authorization failed.")