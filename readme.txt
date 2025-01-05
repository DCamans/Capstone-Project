Welcome to my first ever python project, Naughts and Crosses!

This simple game displays a grid system in which the user can select numbers 1-9 to mark their next move. The computer opponent then randomly selects their next move. This is repeated until a victory condition is met, or the game results in a draw, in which case you have the option to play again.

I created a number of functions which are reused after each round. Having a while loop means that I can run the game until a victory condition or draw occurs. This also means I can display the updated grid after each iteration of the loop, reflecting the current status of the game.

Potential improvements:
For future consideration, I could implement smarter computer decisions, such that it will not select a grid randomly if that choice has no chance of winning. This could potentially look like a series of if statements that prevent an input given the status of the other grids in the row/column/diagonal line.