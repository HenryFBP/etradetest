"""This Python script provides examples on using the E*TRADE API endpoints"""
from __future__ import print_function

import logging
import webbrowser
from logging.handlers import RotatingFileHandler

from rauth import OAuth1Service

import someutils
from accounts.accounts import Accounts
from configlib import CONFIG_CHOICES, get_config
from market.market import Market

# logger settings
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("python_client.log", maxBytes=5 * 1024 * 1024, backupCount=3)
FORMAT = "%(asctime)-15s %(message)s"
fmt = logging.Formatter(FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(fmt)
logger.addHandler(handler)


def oauth(config):
    """Allows user authorization for the sample application with OAuth 1"""
    oauth = OAuth1Service(
        name="etrade",
        consumer_key=config["DEFAULT"]["CONSUMER_KEY"],
        consumer_secret=config["DEFAULT"]["CONSUMER_SECRET"],
        request_token_url="https://api.etrade.com/oauth/request_token",
        access_token_url="https://api.etrade.com/oauth/access_token",
        authorize_url="https://us.etrade.com/e/t/etws/authorize?key={}&token={}",
        base_url="https://api.etrade.com")

    menu_items = {"1": "Sandbox Consumer Key",
                  "2": "Live Consumer Key",
                  "3": "Exit"}
    while True:
        print("")
        options = menu_items.keys()
        for entry in options:
            print(entry + ")\t" + menu_items[entry])
        selection = input("Please select Consumer Key Type: ")
        if selection == "1":
            etrade_url = config["DEFAULT"]["SANDBOX_BASE_URL"]
            break
        elif selection == "2":
            etrade_url = config["DEFAULT"]["PROD_BASE_URL"]
            break
        elif selection == "3":
            raise Exception("goodbye :)")
        else:
            print("Unknown Option Selected!")
    print("")

    # Step 1: Get OAuth 1 request token and secret
    request_token, request_token_secret = oauth.get_request_token(
        params={
            "oauth_callback": "oob",
            "format": "json",
            "credentials": "omit", #YOINK from https://stackoverflow.com/questions/66415479/etrade-api-invalid-consumer-key-and-or-session-token
        })

    # Step 2: Go through the authentication flow. Login to E*TRADE.
    # After you login, the page will provide a text code to enter.
    authorize_url = oauth.authorize_url.format(oauth.consumer_key, request_token)
    webbrowser.open(authorize_url)
    text_code = input("Please accept agreement and enter text code from browser: ")

    # Step 3: Exchange the authorized request token for an authenticated OAuth 1 session
    session = oauth.get_auth_session(request_token,
                                     request_token_secret,
                                     params={"oauth_verifier": text_code})

    main_menu(session, config, etrade_url)


def main_menu(session, config, base_url):
    """
    Provides the different options for the sample application: Market Quotes, Account List

    :param base_url: ETrade URL
    :param session: authenticated session
    """

    menu_items = {"1": "Market Quotes",
                  "2": "Account List",
                  "3": "Exit"}

    while True:
        print("")
        options = menu_items.keys()
        for entry in options:
            print(entry + ")\t" + menu_items[entry])
        selection = input("Please select an option: ")
        if selection == "1":
            market = Market(session, base_url)
            market.quotes()
        elif selection == "2":
            accounts = Accounts(config, session, base_url)
            accounts.account_list()
        elif selection == "3":
            break
        else:
            print("Unknown Option Selected!")


if __name__ == "__main__":
    selected_config_fn = someutils.user_choose_dict(CONFIG_CHOICES, "Please select a config path:")

    if not selected_config_fn:
        raise Exception("Quitting.")

    selected_config = selected_config_fn()

    oauth(selected_config)
