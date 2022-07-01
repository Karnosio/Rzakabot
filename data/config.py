from environs import Env

env = Env()
env.read_env()

VERSION = '0.1'
API_TOKEN = env.str("BOT_TOKEN")
ADMIN_ID = env.list("ADMINS")
