from pathlib import Path
from envparse import env

base_dir: Path = Path(__file__).parent.parent

env.read_envfile(base_dir / ".env")

MONGODB_URL = env.str("MONGODB_URL")
MONGODB_NAME = env.str("MONGODB_NAME")
MONGODB_COLLECTION = env.str("MONGODB_COLLECTION")
