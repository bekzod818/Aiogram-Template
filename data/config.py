from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
PROVIDER_TOKEN = env.str("PROVIDER_TOKEN")  # Payments CLICK token
PROVIDER_TOKEN_PAY_ME = env.str("PROVIDER_TOKEN_PAY_ME") # Payme token
