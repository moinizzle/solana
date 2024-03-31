import sys
from solana.rpc.api import Client
import solders
import json

if len(sys.argv) != 2:
    print("Usage: python getRecipients.py <token_address>")
    sys.exit(1)

token_address = sys.argv[1]
token_address_pubkey = solders.pubkey.Pubkey.from_string(token_address)

client = Client("https://api.mainnet-beta.solana.com")

signatures_resp = client.get_signatures_for_address(token_address_pubkey).to_json()

json_data = json.loads(signatures_resp)

signatures = [item['signature'] for item in json_data['result']]

print("Signatures:")
for signature in signatures:
    print(signature)
