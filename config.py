import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "cricbuzz-cricket.p.rapidapi.com")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/cricket.db")
BASE_API_URL = f"https://{RAPIDAPI_HOST}"
