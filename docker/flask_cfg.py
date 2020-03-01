from environs import Env


env = Env()
env.read_env()

YOUR_ENV_VARIABLE = env("YOUR_ENV_VARIABLE", "DEFAULT_VALUE")
FLASK_ENV = env("FLASK_ENV", "production")
