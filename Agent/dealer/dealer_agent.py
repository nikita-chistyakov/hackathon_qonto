"""
Dealer agent module for the blackjack game.
"""

import os
from typing import Dict, Any
from Agent.dust.utils import get_agent_configuration, save_agent_config

class DealerAgent:
    """Dealer agent for the blackjack game."""
    
    def __init__(self, agent_id: str, config_dir: str = "configs"):
        """Initialize the dealer agent.
        
        Args:
            agent_id: The ID of the agent in Dust.
            config_dir: The directory to save configurations to.
        """
        self.agent_id = agent_id
        self.config_dir = config_dir
        self.config = self._load_configuration()
        self._save_configuration()
    
    def _load_configuration(self) -> Dict[str, Any]:
        """Load the agent's configuration from Dust."""
        return get_agent_configuration(self.agent_id)
    
    def _save_configuration(self) -> str:
        """Save the agent's configuration to a JSON file.
        
        Returns:
            The path to the saved configuration file.
        """
        return save_agent_config(self.agent_id, self.config, self.config_dir)
    
    def get_instructions(self) -> str:
        """Get the agent's instructions.
        
        Returns:
            The agent's instructions.
        """
        return self.config.get("agentConfiguration", {}).get("instructions", "")
    
    def get_model(self) -> str:
        """Get the agent's model.
        
        Returns:
            The agent's model information.
        """
        model_config = self.config.get("agentConfiguration", {}).get("model", {})
        return f"{model_config.get('providerId', '')}/{model_config.get('modelId', '')}"
    
    def get_tools(self) -> Dict[str, Any]:
        """Get the agent's tools.
        
        Returns:
            The agent's tools configuration.
        """
        return self.config.get("agentConfiguration", {}).get("actions", {}) 