
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv('hostname'))
print(os.getenv('ENGINE'))
host=os.getenv('hostname')
