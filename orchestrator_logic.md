A Python script that interacts with an AI agent on Dust to simulate a Game Master (GM) and two players (Player1 and Player2), where:

- Each player has their own private conversation with the GM

- The context is not shared between players — only between the GM and each player separately

- The script should simulate or handle interactions between all three characters via Dust

Here’s a base script to get you started 👇

🧠 Assumptions:
- You already have Dust agents set up for the GM, Player1, and Player2

- You have API keys or credentials to interact with the Dust API

- You want the conversation to alternate: GM ↔️ Player1, GM ↔️ Player2, without leaking context across players

*Python code in "orchestrator.api" file
