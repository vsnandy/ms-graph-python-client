from configparser import ConfigParser
import dotenv
import os

dotenv.load_dotenv()

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('graph_api')

# Set the Values.
config.set('graph_api', 'client_id', os.environ['azure_client_id'])
config.set('graph_api', 'client_secret', os.environ['azure_client_secret'])
config.set('graph_api', 'redirect_uri', os.environ['azure_redirect_uri'])

# Write the file.
with open(file='config.ini', mode='w+') as f:
    config.write(f)
