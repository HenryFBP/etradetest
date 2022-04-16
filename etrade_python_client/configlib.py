import configparser
import os


def get_config() -> configparser.ConfigParser:
    conf_path = '~/.etrade/config.secret.ini'
    conf_path = os.path.abspath(os.path.expanduser(conf_path))
    if not (os.path.exists(conf_path)):
        raise Exception("Please create a file at " + conf_path)

    # loading configuration file
    config = configparser.ConfigParser()
    config.read(os.path.abspath(conf_path))
    return config


CONFIG = get_config()
