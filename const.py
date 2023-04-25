import os
from dotenv import load_dotenv

load_dotenv()

SP_API_REFRESH_TOKEN = os.environ["SP_API_REFRESH_TOKEN"]
LWA_APP_ID = os.environ["LWA_APP_ID"]
LWA_CLIENT_SECRET = os.environ["LWA_CLIENT_SECRET"]
SP_API_ACCESS_KEY = os.environ["SP_API_ACCESS_KEY"]
SP_API_SECRET_KEY = os.environ["SP_API_SECRET_KEY"]
SP_API_ROLE_ARN = os.environ["SP_API_ROLE_ARN"]

GOOGLE_SHEETS_ID = os.environ["GOOGLE_SHEETS_ID"]
GOOGLE_WORKSHEET_NAME = os.environ["GOOGLE_WORKSHEET_NAME"]