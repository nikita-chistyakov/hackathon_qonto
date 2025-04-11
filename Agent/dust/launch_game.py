import os
import utils    
import json
import time
class Game:
    def __init__(self):
        self.conversation = None
        self.dealer_agent_id = os.getenv("DEALER_AGENT_ID")
        self.player_agent_id = os.getenv("PLAYER_AGENT_ID")
        self.workspace_id = os.getenv("DUST_WORKSPACE_ID")
        self.api_key = os.getenv("DUST_API_KEY")
        self.base_url = os.getenv("DUST_BASE_URL", "https://dust.tt")
        self.num_players = 3
        self.init_players()
        self.message = self.create_dealer()
        self.is_game_running = True
        self.process_message(self.dealer_conversation_id)
    

    def create_dealer(self):
        self.dealer_conversation_id = utils.create_conversation(self.dealer_agent_id, "Hello, I am the dealer. Let's play a game of Liar's Dice!")["conversation"]["sId"]
        utils.create_message(self.dealer_conversation_id, "Hello, I am the dealer. Let's play a game of Liar's Dice!", self.dealer_agent_id)
    
    def init_players(self):
        self.players = {id : {"conversation_id": None, "agent_id": self.player_agent_id} for id in range(self.num_players)}
        for i in range(self.num_players):
            player_conversation_id = utils.create_conversation(self.player_agent_id, "Hello, I am the player. Let's play a game of Liar's Dice!")["conversation"]["sId"]
            self.players[i]["conversation_id"] = player_conversation_id

    def process_message(self, next_conversation_id: str , i = 0):
        """Process messages from the conversation.
        
        Args:
            next_conversation_id: The ID of the conversation to process messages from
            
        Returns:
            The processed message content
        """
        print("waiting 30 seconds")
        time.sleep(30)
        i = 0
        while i < 10: #self.is_game_running:
            i += 1
            self.message = utils.get_conversation_last_message(next_conversation_id)
            print("message",self.message)      
            # Check if message is in JSON format        
            try:
                message_dict = json.loads(self.message)
                if "player" in message_dict and "prompt" in message_dict:
                    next_conversation_id = self.players[int(message_dict["player"].replace("Player", "")-1)]["conversation_id"]
                    utils.create_message(next_conversation_id, message_dict["prompt"], self.player_agent_id)
                    self.process_message(next_conversation_id,i)

            except json.JSONDecodeError:
                next_conversation_id = self.dealer_conversation_id 
                utils.create_message(next_conversation_id, self.message, self.dealer_agent_id)
                self.process_message(next_conversation_id,i)


   
if __name__ == "__main__":
    print("Starting game")
    game = Game()
    

    
        
