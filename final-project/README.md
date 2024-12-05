# Tetris Game
## CS110 Final Project  Fall, 2024

## Team Members

Cheng Jie Yau

***

## Project Description

Clone of the tetris game that will include features for score tracking, lines mades, viewing upcoming blocks and level counter. The fall speed of the blocks will also increase as the level increases. The gui design will look similar to that of the image provided in assets.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Pause Menu
2. Gameover Screen
3. Score Tracker
4. Line Counter
5. Block Preview

### Classes
Controller
Preview
Game
Score
Timer
Tetromino
-

## ATP
Test Case 1: Tetromino movement/rotation/drop
Test Description: Verify that the tetromino block moves left, right, down, drops and rotates as expected.
Test Steps:
1. Start the game.
2. Press the left arrow key.
3. Verify that the tetromino block moves left.
4. Press the right arrow key.
5. Verify that the tetromino block moves right.
6. Press the up arrow key a few times.
7. Verify that the tetromino block can rotate as desired.
8. Press the down arrow key.
9. Verify that the tetromino block moves down 1 row.
10. Press the space bar.
11. Verify that the tetromino block instantly drops to the bottom and the next block appears.

Expected Outcome: The tetromino block should be able to move left, right, down, or rotate in response to the arrow key inputs and drop in response to the space bar.

Test case 2: Gameover
Test Description: Verify that the gameover screen appears with option to play again
1. Start the game.
2. Continously press the spacebar to drop tetromino blocks.
3. Repeat until the tetromino blocks stack to the top.
4. Verify that this triggers the gameover screen
5. Press the R key.
6. Verify this restarts the game.

Expected Outcome: Once the tetromino blocks reach the top of the game grid, the gameover screen should appear and the game restarts in response to the R key.

Test case 3: Row clear, score and line tracker functionality
Test Description: Verify that the rows clear when completed and the score and line tracker update accordingly.
1. Start the game.
2. Play the game by fitting the tetromino blocks together to fill a row.
3. Keep trying until a single row has been filled.
4. Verify that completing a row clears the line.
6. Verify that the score increases.
7. Verify that the line tracker updates accordingly.

Expected Outcome: When a row is filled, the row should clear and the score should increase with the line tracker updating accordingly.

Test case 4: Pause Test
Test Description: Verify that the pause key works.
1. Start the game.
2. Press the P key.
3. Verify that the game has paused and the pause screen appears.
4. Press the P key again.
6. Verify that the game resumes from where you left off.

Expected Outcome: In response to the P key, the game should pause and a pause screen should appear. By pressing the P key again, the game should resume.

Test case 5: Preview Box
Test description: Verify the peview box updates after placing a tetromino block down.
1. Start the game.
2. Look at the preview box to the top right of the window.
3. Note the blocks on it currently.
4. Press spacebar to instantly drop a tetrimino block.
5. Look at the preview box again.
6. Verify that a new block has appeared.

Expected Outcome: The preview box should have a new tetrimino block on display every time the user drops a block.
