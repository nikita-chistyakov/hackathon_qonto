"""
Utility functions for interacting with Dust API.
"""

import os
import json
import requests
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_agent_configuration(agent_id: str) -> Dict[str, Any]:
    """Get the configuration for a specific agent.
    
    Args:
        agent_id: The ID of the agent to get configuration for
        
    Returns:
        Dict containing the agent's configuration
        
    Raises:
        ValueError: If required environment variables are not set
        requests.exceptions.RequestException: If the API request fails
    """
    # Get required environment variables
    workspace_id = os.getenv("DUST_WORKSPACE_ID")
    api_key = os.getenv("DUST_API_KEY")
    base_url = os.getenv("DUST_BASE_URL", "https://api.dust.tt")
    
    if not all([workspace_id, api_key]):
        raise ValueError("DUST_WORKSPACE_ID and DUST_API_KEY must be set in .env file")
    
    # Construct the API URL
    url = f"{base_url}/api/v1/w/{workspace_id}/assistant/agent_configurations/{agent_id}"
    
    # Set up headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Make the request
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()

def save_agent_config(agent_id: str, config: Dict[str, Any], output_dir: str = "configs") -> str:
    """Save agent configuration to a JSON file.
    
    Args:
        agent_id: The ID of the agent
        config: The agent configuration to save
        output_dir: Directory to save the configuration file (default: "configs")
        
    Returns:
        Path to the saved configuration file
        
    Raises:
        OSError: If the output directory cannot be created
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create filename
    filename = f"{agent_id}_config.json"
    filepath = os.path.join(output_dir, filename)
    
    # Save configuration to file
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=2)
    
    return filepath 

def create_conversation(agent_id: str, initial_message: str = "Hello!") -> Dict[str, Any]:
    """Create a new conversation with a specified agent.
    
    Args:
        agent_id: The ID of the agent to create conversation with. Should be either
                 PLAYER_AGENT_ID or DEALER_AGENT_ID from environment variables.
        initial_message: The first message to send in the conversation (default: "Hello!")
        
    Returns:
        Dict containing the created conversation data
        
    Raises:
        ValueError: If required environment variables are not set or invalid agent_id provided
        requests.exceptions.RequestException: If the API request fails
    """
    # Get required environment variables
    workspace_id = os.getenv("DUST_WORKSPACE_ID")
    api_key = os.getenv("DUST_API_KEY")
    base_url = os.getenv("DUST_BASE_URL", "https://dust.tt")
    
    if not all([workspace_id, api_key]):
        raise ValueError("DUST_WORKSPACE_ID and DUST_API_KEY must be set in .env file")
    
    # Validate agent_id
    # player_agent = os.getenv("PLAYER_AGENT_ID")
    # dealer_agent = os.getenv("DEALER_AGENT_ID")
    # if agent_id not in [player_agent, dealer_agent]:
    #     raise ValueError("agent_id must be either PLAYER_AGENT_ID or DEALER_AGENT_ID from .env")
    
    # Construct the API URL
    url = f"{base_url}/api/v1/w/{workspace_id}/assistant/conversations"
    
    # Set up headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare request payload
    payload = {
        "title": "Game Rules Discussion New",
        "visibility": "unlisted",
        "blocking": True,
        "messages": {
            "content": initial_message,
            "mentions": [{"configurationId": agent_id}],
            "context": {
                "username": "max",
                "timezone": "Europe/Paris"
            }
        },
    
        
       
    }
    
    # Make the request
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def create_message(conversation_id: str, message: str, agent_sId: str) -> Dict[str, Any]:
    """Create a new message in a specified conversation.
    
    Args:
        conversation_id: The ID of the conversation to create the message in
        message: The content of the message to create
    """
    wId = os.getenv("DUST_WORKSPACE_ID")
    url =   f"https://dust.tt/api/v1/w/{wId}/assistant/conversations/{conversation_id}/messages"
    api_key = os.getenv("DUST_API_KEY")
    headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    payload = {
        "content": message,
        "mentions": [{"configurationId": agent_sId}],
        "context": {
            "username": "max",
            "timezone": "Europe/Paris"
            }   
    }
    requests.post(url, headers=headers, json=payload)

def get_conversation_last_message(conversation_id: str) -> Dict[str, Any]:
    """Get all messages from a specified conversation.
    
    Args:
        conversation_id: The ID of the conversation to get messages from

    Returns:
        Dict containing the messages from the conversation
    """
    wId = os.getenv("DUST_WORKSPACE_ID")
    url =   f"https://dust.tt/api/v1/w/{wId}/assistant/conversations/{conversation_id}"
    api_key = os.getenv("DUST_API_KEY")
    headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    # return last message
    response = requests.get(url, headers=headers).json()
    response_message = response['conversation']['content'][-1][0]['content']
    return response_message