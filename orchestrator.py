import requests

# Config: replace with your real values
DUST_API_URL = "https://dust.tt/api/run"
DUST_API_KEY = "your_dust_api_key"

AGENTS = {
    "gm": "your_gm_agent_id",
    "player1": "your_player1_agent_id",
    "player2": "your_player2_agent_id"
}

HEADERS = {
    "Authorization": f"Bearer {DUST_API_KEY}",
    "Content-Type": "application/json"
}

# Maintain separate chat histories
chat_gm_p1 = []
chat_gm_p2 = []

def send_message(agent_id, messages):
    """
    Send messages to a Dust agent and get the response.
    """
    payload = {
        "agent_id": agent_id,
        "messages": messages
    }
    response = requests.post(DUST_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["message"]

def gm_player_interaction(chat_history, player_name):
    """
    Facilitates turn between GM and a player (player1 or player2).
    """
    # Last message from player
    last_player_msg = chat_history[-1]["content"] if chat_history else f"Hello, I am {player_name}. Let's begin."

    # GM responds
    gm_input = [{"role": "user", "content": last_player_msg}]
    gm_response = send_message(AGENTS["gm"], gm_input)
    chat_history.append({"role": "assistant", "content": gm_response})

    # Player replies
    player_input = [{"role": "user", "content": gm_response}]
    player_response = send_message(AGENTS[player_name], player_input)
    chat_history.append({"role": "user", "content": player_response})

    return gm_response, player_response

# Run a sample interaction loop
for turn in range(3):  # 3 turns for demo
    print(f"--- Turn {turn + 1}: Player 1 ---")
    gm_msg, p1_msg = gm_player_interaction(chat_gm_p1, "player1")
    print("GM:", gm_msg)
    print("Player 1:", p1_msg)

    print(f"--- Turn {turn + 1}: Player 2 ---")
    gm_msg, p2_msg = gm_player_interaction(chat_gm_p2, "player2")
    print("GM:", gm_msg)
    print("Player 2:", p2_msg)
