from notion.client import NotionClient

# Replace with your Notion API token
NOTION_TOKEN = 'secret_NiTxaxUJlOK5NvAzll0lVLDz6NfFE7fvpnBDPr9cQVT'

# Replace with your database ID
DATABASE_ID = 'a0578abe99744e91bb901bfe6b5abfe5'

# Initialize the Notion client
client = NotionClient(auth=NOTION_TOKEN)

# Query the database
database = client.databases.query(database_id=DATABASE_ID)

# Print the response (you can process it further as needed)
print(database)
