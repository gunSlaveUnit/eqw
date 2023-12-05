from pathlib import Path

from server.src.settings import HOST, PORT

BASE_PATH = Path(__file__).resolve().parent
RESOURCES_PATH = BASE_PATH / "resources"
ICONS_PATH = RESOURCES_PATH / "icons"

SERVER_URL = f"http://{HOST}:{PORT}/"
AUTH_URL = SERVER_URL + "auth/"
REGISTER_URL = AUTH_URL + "sign-up/"
LOGIN_URL = AUTH_URL + "sign-in/"
LOGOUT_URL = AUTH_URL + "sign-out/"
ME_URL = AUTH_URL + "me/"
CHECK_URL = SERVER_URL + 'check/'
CHECKS_URL = CHECK_URL + 'checks/'
ONE_CHECK_URL = CHECK_URL + 'check/'
ATTACK_URL = SERVER_URL + 'attack/'
