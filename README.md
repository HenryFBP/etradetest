# actually read this :3c you silly goose

copy `config.example.ini` to:

    ~/.etrade/config.production.secret.ini
    ~/.etrade/config.sandbox.secret.ini

amnd fill it in w/ your etrade api key and secret. get API keys at <https://developer.etrade.com/home>

# Running

    pip install poetry
    poetry install
    poetry shell
    python .\EtradeTest\

# update deps

    poetry update

# links

see [./README-old.md](./README-old.md) for old shit

- <https://www.youtube.com/watch?v=6pGUFM9yqWo>
- <https://www.youtube.com/watch?v=lwJoPxOL_Zw>
  - <https://github.com/jordanshadowens/buylowsellhigh>

# issues

## http 401

You may have an expired token: <https://github.com/jessecooper/pyetrade/issues/52>

If it's older than 2 years... its dead becauasesusuuse
ETrade engineers are too lazy to make automated key mgmt mechanisms ;3c

either email them or make a new account...I figured the latter was faster :P
