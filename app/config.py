from starlette.config import Config

config = Config(".env")

try:
    API_PREFIX: str = config("API_PREFIX")
    API_HOST: str = config("API_HOST")
    API_PORT: int = config("API_PORT", cast=int)

    _db_h = config("DB_HOST")
    _db_d = config("DB_NAME")
    _db_u = config("DB_USER")
    _db_p = config("DB_PASSWORD")
    DB_URL: str = f"postgresql+asyncpg://{_db_u}:{_db_p}@{_db_h}/{_db_d}"
except Exception as e:
    print(f"Config error: {e}")
    exit(1)
