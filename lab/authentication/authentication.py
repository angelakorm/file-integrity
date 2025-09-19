from msal import PublicClientApplication
from config import Config

def get_token():
    app = PublicClientApplication(client_id=Config.CLIENT_ID, authority=Config.AUTHORITY)

    result = None
    accounts = app.get_accounts()
    if accounts:
        print("Pick the account you want to use to proceed:")
        for a in accounts:
            print(a["username"])
        chosen = accounts[0]
        result = app.acquire_token_silent([Config.SCOPES], account=chosen)

    if not result:
        print("No suitable token in cache found, getting a new one from Azure AD.")
        result = app.acquire_token_interactive(scopes=[Config.SCOPES], prompt="select_account")

    if "access_token" in result:
        print("Authentication success. This is your token: ")
        print(result["access_token"])
        return result["access_token"]
    else:
        raise Exception("Authorization failed.")
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))