### Objectives
The dealer's objective is to orchestrate conversations between different players and provide them with the dice rolls, the correct context, and to make sure that they respect the rules of the game. The player's objective is to be the last player standing at the end of the game.

### Gameplay
The dealer sets up the game with three players. For each player, the dealer then rolls three six-sided dice corresponding to each player, for instance: 

The dealer then indicates who plays first, and tells them what dice they have and what to do. 

```json
{
    "player": "Player1",
    "prompt": "Player1 takes the first turn. Player1's dice are 1,2,6"
}
```

The first player makes a bid consisting of a quantity (how many dice) and a face value (which number on the dice). The bid represents the overall dice on the table, not just the players. As an example, "two 6s" means they believe there are at least two dice showing 6 across all players. 

```txt
Player1: 2D6
```

Dealer summarizes the bets, indicates the next players what dice they have, and indicates who plays next, for instance:
```json
{
    "player": "Player2",
    "prompt": "Player1's bet was 2D6. Player2's dice are 6,2,4."
}
```

The second player, along with every subsequent player, is provided with two options: 
- Raising the Bid: Make a higher bid
- Challenge the Bid: Challenge the previous bid by calling "Liar!"

Raising the bid can ONLY be done in these ways:
    Same quantity of a higher face (e.g., "two 5s" after "two 4s")
    Higher quantity of the same face (e.g., "three 4s" after "two 4s")
    Higher quantity of a higher face (e.g., "three 5s" after "two 4s")

For instance, the player's response is: 
```txt
Player2: 3D6
```

When a challenge occurs:
    All players reveal their dice
    If the bid is matched or exceeded, the bidder wins
    If the bid is not met, the challenger wins

For instance, the player's response is: 
```txt
Player:2: Player1 is a liar. 
```

If the bid was raised, Dealer summarizes the bets, indicates the next players what dice they have, and indicates who plays next, for instance:
```json
{
    "player": "Player3",
    "prompt": "Player1's bet was 2D6, player2's bet was 3D6. Player2's dice are 6,2,4."
}
```

If the player challenged the bet, dealer reveals all dice and evaluates who wins and who loses. The loser of a challenge loses one die and will roll one fewer die during their next round. The loser starts the next round. 

For instance:
```json
{
    "player": "Player3",
    "prompt": "Player1's bet was 2D6, player2's challenged the bid.
Dice rolls: 
- Player1: 3,1,4
- Player2: 2,2,
- Player3: 2,3,2

Player2 loses a die ! Player2 takes the first turn
player1 dice: 1,2,6"
}
```

When only one players remain in play with dice remaining, the game ends. 

### Important Notes
Both the player's responses are exclusively in JSON format. They do not indicate their reasoning nor do they remind the rules to the other players.  
When a bet is forbidden or unclear, repeat the exact same request again.  
