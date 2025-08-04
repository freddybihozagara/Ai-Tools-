from dotenv import load_dotenv
import os

def init_env():
    # Load environment variables from .env.local
    load_dotenv('.env.local')
    
    # Verify required environment variables
    required_vars = [
        'SITE_URL',
        'KEY',
        'DB_HOST',
        'DB_USER',
        'DB_PWD',
        'DB_PORT',
        'DB_NAME',
        'APP_PORT',
        'DEBUG'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}")

    return {
        'SITE_URL': os.getenv('SITE_URL'),
        'KEY': os.getenv('KEY'),
        'DB_HOST': os.getenv('DB_HOST'),
        'DB_USER': os.getenv('DB_USER'),
        'DB_PWD': os.getenv('DB_PWD'),
        'DB_PORT': int(os.getenv('DB_PORT')),
        'DB_NAME': os.getenv('DB_NAME'),
        'APP_PORT': int(os.getenv('APP_PORT')),
        'DEBUG': os.getenv('DEBUG').lower() == 'true'
    }