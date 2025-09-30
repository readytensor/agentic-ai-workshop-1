from dotenv import load_dotenv
import os

from pathlib import Path

ENV_FPATH = Path(__file__).parent.parent.parent.parent / ".env"


def load_env(api_key_type="OPENAI_API_KEY") -> None:
    """Loads environment variables from a .env file and checks for required keys.

    Raises:
        AssertionError: If required keys are missing.
    """
    # Load environment variables from .env file
    load_dotenv(ENV_FPATH, override=True)

    # Check if 'XYZ' has been loaded
    api_key = os.getenv(api_key_type)

    assert (
        api_key
    ), f"Environment variable '{api_key_type}' has not been loaded or is not set in the .env file."

    print(f"Environment variable '{api_key_type}' has been loaded successfully.")
