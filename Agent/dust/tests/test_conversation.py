import os
import sys
import json
import requests
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))
from utils import create_conversation

def test_create_conversation_with_rules():
    # Get the dealer agent ID from environment variables
    dealer_agent_id = os.getenv("DEALER_AGENT_ID")
    
    message = "say hi"
    # Create a conversation with the dealer agent using the rules as initial message
    response = create_conversation(
        agent_id=dealer_agent_id ,
        initial_message=message 
    )
    # Print the complete response for debugging
    print("\nComplete API Response:")
    print(json.dumps(response, indent=2))
    return response

   
if __name__ == "__main__":
    
    cId = "9PtamaS6X0"
    wId = os.getenv("DUST_WORKSPACE_ID")
    url =   f"https://dust.tt/api/v1/w/{wId}/assistant/conversations/{cId}"
    api_key = os.getenv("DUST_API_KEY")
    headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    response = requests.get(url, headers=headers)
    
    print(response.json()['conversation']['content'][-1][0]['content'])
    return response.json()['conversation']['content'][-1][0]['content']

