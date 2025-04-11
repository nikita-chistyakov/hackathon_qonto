import requests
import json

# Configuration
API_KEY = "sk-df7af10f140046fe46ac168f81c2a2f8"
WORKSPACE_ID = "46d7335c2e"
BASE_URL = "https://dust.tt/api/v1"

def list_conversations():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}/workspaces/{WORKSPACE_ID}/conversations"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        conversations = response.json()
        
        if not conversations:
            print("No conversations found.")
            return
            
        print("\nConversations in workspace:")
        print("-" * 50)
        for conv in conversations:
            print(f"Title: {conv.get('title', 'Untitled')}")
            print(f"ID: {conv.get('id')}")
            print(f"Created at: {conv.get('created_at')}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversations: {e}")

if __name__ == "__main__":
    list_conversations() 