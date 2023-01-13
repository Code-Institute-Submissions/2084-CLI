This is an implementaion of the popular 2048 game. This version is a command line interface built in Python.

## How To Play

* The user must press h,j,k,l to move up/down/left/right
* The aim is to achieve the highest number possible by adding numbers together
* Numbers can only be added if:
  - they are the same number and
  - they are adjacent cells or separated by only 0s

## Features

# The board
The game contains a 4 X 4 'grid'. At the beginning of the game, the grid will contain a single cell with the value of '2'. Each time the player moves, another 2 will appear on the grid. 

  ![Grid](/assets/images/grid.png)

# Directional Buttons
The CLI contains information on which buttons will move the board in each direction

  ![Grid](/assets/images/buttons.png)

# Game Over Message
When the board is full and can no longer move, the message 'Game Over' will appear. If the users has achieved a new high score, the leaderboard which is stored in Google Sheets will be updated.

  ![Grid](/assets/images/game-over.png)


## Unfixed Bugs

1. Move left/right merge functionality issue
  - cell merge when moving left and right is not fluid
  - only the first cells which are directly beside each other will merge
  - the buttons must be pressed multiple times to merge all cells

## Future Features to Implement

1. Create a 'User Name' input and save name to the Leaderboard if user reaches a high score
2. Style grid to have boarders between each cell

# Testing

Testing of functions achieved using 'unittest' library. 






* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!