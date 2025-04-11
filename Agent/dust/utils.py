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