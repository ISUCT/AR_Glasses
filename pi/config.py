import os
from dotenv import load_dotenv

if os.path.exists('.env'):
    load_dotenv('.env')

ENVIRONMENT_STATE = os.getenv('ENVIRONMENT_STATE')