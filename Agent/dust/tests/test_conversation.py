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
    
    # Get the path to the rules file
    current_dir = Path(__file__).parent
    rules_path = current_dir.parent.parent / "prompts" / "rules.md"
    
    # Read the rules file
    with open(rules_path, "r") as f:
        rules_content = f.read()

    rules_content = rules_content + " let's start the game"
    print(rules_content)
    # Create a conversation with the dealer agent using the rules as initial message
    response = create_conversation(
        agent_id=dealer_agent_id,
        initial_message=rules_content
    )
    # Print the complete response for debugging
    print("\nComplete API Response:")
    print(json.dumps(response, indent=2))
   