import os
import pytest
import sys
import json
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
        agent_id=dealer_agent_id,
        initial_message=message 
    )
    # Print the complete response for debugging
    print("\nComplete API Response:")
    print(json.dumps(response, indent=2))
   
if __name__ == "__main__":
    test_create_conversation_with_rules()