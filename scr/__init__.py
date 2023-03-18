from flask import Flask

app = Flask(__name__)
app.config.from_object('scr.config')

import scr.views