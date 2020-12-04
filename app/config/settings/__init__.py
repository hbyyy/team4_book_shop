import os

prod = os.environ.get('BOOKMARKET_PROD')

if prod:
    from .prod import *
else:
    from .dev import *
