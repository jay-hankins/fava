from flask_behind_proxy import FlaskBehindProxy

from fava.application import app

FlaskBehindProxy(app)
app.config["BEANCOUNT_FILES"] = ["/home/jay/dev/fava/ledger.beancount"]
