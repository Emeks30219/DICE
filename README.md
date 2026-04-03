# 🎲 Dice Rolling Game
 
A Python-based multiplayer dice rolling game for 2–4 players. Players take turns rolling a die and accumulating points. The first player to reach **50 points** wins!
 
---
 
## 📋 How to Play
 
1. Launch the game and enter the number of players (between 2 and 4).
2. On your turn, choose whether to roll the die or stop.
3. Each roll adds to your **turn score** — but if you roll a **1**, you lose all points for that turn!
4. When you stop rolling, your turn score is added to your **total score**.
5. The first player to reach or exceed **50 points** wins the game.
 
---
 
## ⚙️ Features
 
- Supports **2 to 4 players**
- Input validation — handles invalid entries gracefully
- Risk-based gameplay: keep rolling to score more, or stop to bank your points
- Automatic winner detection at the end of the game
 
---
 
## 🚀 Getting Started
 
### Prerequisites
 
- Python 3.x installed on your machine
 
### Run the Game
 
```bash
python dice_game.py
```
 
---
 
## 🕹️ Gameplay Example
 
```
Enter the number of players (2-4): 3
 
Player number 1 turn has just started!
 
Would you like to roll? (y/n): y
You rolled a: 4
Your current turn score is: 4
 
Would you like to roll? (y/n): y
You rolled a: 1
You rolled a 1! Turn over, no points added.
 
Your total score is: 0
 
Player number 2 turn has just started!
...
 
Player 2 wins with a score of 52!
```
 
---
 
## 📁 Project Structure
 
```
dice_game.py # Main game file
README.md # Project documentation
```
 
---
 
## 🐛 Known Bugs Fixed
 
This project went through a debugging pass. The following issues were resolved:
 
| Bug | Fix Applied |
|-----|-------------|
| Roll condition was inverted (`!= "y"`) | Changed to `== "y"` |
| Inner `while` loop was outside the `for` loop | Re-indented inside the player `for` loop |
| `value` variable used before assignment | Moved `value = roll()` before the `if/else` check |
| Typos: `player_idk`, `currentscore` | Fixed to `player_idx` and `current_score` |
| No winner announcement at game end | Added winner detection logic |
 
---
 
## 🛠️ Built With
 
- **Python 3** — Core language
- **`random` module** — For dice roll simulation
 


