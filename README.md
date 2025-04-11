# hackathon_qonto
AI Dust agent 

## Perudo_ai 
Play Liar's dice against a set of Dust Agents in the Dust chat. 

## Credentials 
Domain
https://dust.tt

Workspace ID
46d7335c2e

API Key
sk-df7af10f140046fe46ac168f81c2a2f8

## Liar's Dice Game Rules

### Setup
    Each player gets 3 six-sided dice (instead of the standard 5)
    Each player needs a dice cup or some way to conceal their dice
    Players roll all their dice simultaneously and keep them hidden
    Players can look at their own dice but must keep them hidden from others

### Gameplay
    The first player makes a bid consisting of:
        A quantity (how many dice)
        A face value (which number on the dice)
        Example: "two 4s" means they believe there are at least two dice showing 4 across all players
    Play proceeds clockwise with each player having two options:
        Raising the Bid: Make a higher bid
        Challenge the Bid: Challenge the previous bid by calling "Liar!"
    Raising the bid can ONLY be done in these ways:
        Same quantity of a higher face (e.g., "two 5s" after "two 4s")
        Higher quantity of the same face (e.g., "three 4s" after "two 4s")
        Higher quantity of a higher face (e.g., "three 5s" after "two 4s")
    When a challenge occurs:
        All players reveal their dice
        If the bid is matched or exceeded, the bidder wins
        If the bid is not met, the challenger wins
    The loser of a challenge loses one die
        The die is removed from play
        The loser starts the next round
    The game continues until only one player has dice remaining

### Important Notes
    No special rules for 1s (they are NOT wild in this variant)
    Each face value (1-6) counts only as itself
    The expected quantity of any face value is 1/6 of the total dice in play


## Selling Points 
- Orchestrate several agents 
- Ensure that random stuff is actually random 
- Compartmentize information within 