# Tic-Tac-Toe with CLIPS AI

This project is a command-line Tic-Tac-Toe game implemented in Python. The game allows a user to play against an AI opponent that utilizes CLIPS (C Language Integrated Production System) to make decisions based on predefined rules. The game is played on a 3x3 grid where players take turns placing their marks (X for the user and O for the AI) until one player wins or the game ends in a draw. To play, just run the script tic-tac-toe.py.

Dependencies can be installed by ttt.yml. 

### How the AI Works

The AI uses CLIPS to make decisions based on predefined rules. It follows these strategies:

- Win if possible: The AI tries to complete a row, column, or diagonal if it has two marks in a line.
- Block the opponent: If the user is about to win, the AI blocks their move.
- Play the center: If the center is available, the AI selects it.
- Play a corner: If a corner is available, the AI chooses it.
- Random move: If no strategic move is available, the AI selects a random open space.

There is only one sequence of movements in which the user actually wins (it woluld't be fun if you always lose), otherwise the AI always wins or draws.
