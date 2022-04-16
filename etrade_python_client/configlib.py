import configparser
import os
import time

SANDBOX_CONFIG_PATH = '~/.etrade/config.sandbox.secret.ini'
PROD_CONFIG_PATH = '~/.etrade/config.production.secret.ini'


def get_config(config_path='~/.etrade/config.sandbox.secret.ini') -> configparser.ConfigParser:
    config_path = os.path.abspath(os.path.expanduser(config_path))
    if not (os.path.exists(config_path)):
        raise Exception("Please create a file at " + config_path)

    # loading configuration file
    config = configparser.ConfigParser()
    config.read(os.path.abspath(config_path))
    return config


def get_sandbox_config():
    return get_config(SANDBOX_CONFIG_PATH)


def get_production_config():
    print("WARNING: This is PROD config! You will be using REAL CASH MONEY...just letting yuo know bro...")
    time.sleep(2)
    return get_config(PROD_CONFIG_PATH)


CONFIG_CHOICES = {
    "1": get_sandbox_config,
    "2": get_production_config,
}
