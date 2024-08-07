from dotenv import load_dotenv
import os

load_dotenv()

print("REFRESH_TOKEN:", os.getenv('REFRESH_TOKEN'))
print("CLIENT_ID:", os.getenv('CLIENT_ID'))
print("CLIENT_SECRET:", os.getenv('CLIENT_SECRET'))