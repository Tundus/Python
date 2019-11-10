import sys, os
sys.path.append(os.path.abspath('../r2d'))

from db_connect import *

drop_db()
create_db()
