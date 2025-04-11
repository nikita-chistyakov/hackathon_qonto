"""
Test script for initializing and testing dealer and player agents.
"""

import os
from dotenv import load_dotenv
from Agent.dealer.dealer_agent import DealerAgent
from Agent.player.player_agent import PlayerAgent

def main():
    load_dotenv()
    
    dealer_agent_id = os.getenv('DEALER_AGENT_ID')
    player_agent_id = os.getenv('PLAYER_AGENT_ID')
    
    if not dealer_agent_id or not player_agent_id:
        print("Error: Please set DEALER_AGENT_ID and PLAYER_AGENT_ID in .env file")
        return
    
    try:
        # Initialize and test dealer agent
        print("\nTesting Dealer Agent:")
        dealer = DealerAgent(dealer_agent_id)
        print(f"Agent ID: {dealer_agent_id}")
        print("Instructions:")
        print("-" * 50)
        print(dealer.get_instructions())
        print("-" * 50)
        print(f"Model: {dealer.get_model()}")
        print(f"Configuration saved to: {dealer._save_configuration()}")
        
        # Initialize and test player agent
        print("\nTesting Player Agent:")
        player = PlayerAgent(player_agent_id)
        print(f"Agent ID: {player_agent_id}")
        print("Instructions:")
        print("-" * 50)
        print(player.get_instructions())
        print("-" * 50)
        print(f"Model: {player.get_model()}")
        print(f"Configuration saved to: {player._save_configuration()}")
        
    except Exception as e:
        print(f"Error during agent initialization: {str(e)}")

if __name__ == "__main__":
    main() 