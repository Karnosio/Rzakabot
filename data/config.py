from environs import Env

env = Env()
env.read_env()

VERSION = '0.1'
API_TOKEN = env.str("BOT_TOKEN")
ADMIN_ID = env.list("ADMINS")

MySQL_db_name = env.str("MySQL_db_name")
MySQL_db_login = env.str("MySQL_db_login")
MySQL_db_password = env.str("MySQL_db_password")
MySQL_db_host = env.str("MySQL_db_host")
