A Python script that interacts with an AI agent on Dust to simulate a Game Master (GM) and two players (Player1 and Player2), where:

- Each player has their own private conversation with the GM

- The context is not shared between players — only between the GM and each player separately

- The script should simulate or handle interactions between all three characters via Dust

🧠 Assumptions:
- Set up Dust agents for the GM, Player1, and Player2

- API keys or credentials to interact with the Dust API

- Want the conversation to alternate: GM ↔️ Player1, GM ↔️ Player2, without leaking context across players

*Python code in "orchestrator.api" file
