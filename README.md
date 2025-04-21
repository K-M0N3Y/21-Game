# 21-Game

A simple Python-based 21-card game where players compete against the dealer to get the highest hand without going over 21.

## Introduction

The 21-Game is a fun and interactive console-based game where a player faces off against a dealer. The objective is to get as close to 21 as possible without exceeding it. Face cards (Jack, Queen, King) are worth 10 points, and Aces can be counted as either 1 or 11. This game is a great way to practice simple game mechanics and Python programming.

## How to Play

1. **Run the game**:
   - If you have Python installed, navigate to the folder where the `game.py` file is located.
   - Open a terminal or command prompt and run the following command:
     ```bash
     python src/game.py
     ```

2. **Gameplay**:
   - Once the game starts, you will be dealt two cards, and the dealer will have one card face-up and one face-down.
   - Your goal is to get a total of 21 or as close as possible without exceeding it.
   - You can type **'Hit'** to get another card or **'Stay'** to stop drawing.
   - If your total goes over 21, you "bust" and lose the game.
   - The dealer will draw cards until their total is 16 or higher.

![Screenshot 2025-04-20 205244](https://github.com/user-attachments/assets/04237539-e751-48af-9522-ca0b4f57e8b8)

3. **Winning the Game**:
   - If your hand is closer to 21 than the dealer’s, you win.
   - If the dealer's total exceeds 21, you win by default.
   - If both you and the dealer have the same total, it's a tie.

![Screenshot 2025-04-20 205353](https://github.com/user-attachments/assets/5207eaf7-06f4-4403-a882-9d7eb04eea23)

4. **Ending the Game**:
   - The game will end when either the player wins, the dealer wins, or both have tied.

![Screenshot 2025-04-20 205411](https://github.com/user-attachments/assets/7e9c2549-15a4-46cd-ac48-1fd722dc016b)   

## Known Issues

- Currently, there is no option for saving game progress. This is something we plan to add in the future.
- The user interface is text-based only; future versions will explore graphical interfaces.

If you encounter any bugs or issues, feel free to submit a new issue or contribute a fix!

---

Thanks for checking out this project! Happy coding and playing!
