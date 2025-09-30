from dotenv import load_dotenv
import os

ENV_FPATH = "../../.env"

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv(ENV_FPATH)
    return True

def get_env_var(var_name, default=None):
    """Get environment variable with optional default"""
    return os.getenv(var_name, default)
