# ------------------------------
# 353. Design Snake Game
# 
# Description:
# Design a Snake game that is played on a device with screen size = width x height. Play 
# the game online if you are not familiar with the game.
# 
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
# You are given a list of food's positions in row-column order. When a snake eats the food, 
# its length and the game's score both increase by 1.
# 
# Each food appears one by one on the screen. For example, the second food will not appear 
# until the first food was eaten by the snake.
# 
# When a food does appear on the screen, it is guaranteed that it will not appear on a block 
# occupied by the snake.
# 
# Example:
# 
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
# Snake snake = new Snake(width, height, food);
# Initially the snake appears at position (0,0) and the food at (1,2).
# 
# |S| | |
# | | |F|
# 
# snake.move("R"); -> Returns 0
# 
# | |S| |
# | | |F|
# 
# snake.move("D"); -> Returns 0
# 
# | | | |
# | |S|F|
# 
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
# 
# | |F| |
# | |S|S|
# 
# snake.move("U"); -> Returns 1
# 
# | |F|S|
# | | |S|
# 
# snake.move("L"); -> Returns 2 (Snake eats the second food)
# 
# | |S|S|
# | | |S|
# 
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
# 
# Version: 1.0
# 11/20/19 by Jianfa
# ------------------------------

from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.n = width
        self.m = height
        self.food = deque(food)
        self.snake = deque([[0, 0]]) # snake[0] is tail, snake[-1] is head
        self.direct = {'U':[-1, 0], 'L':[0, -1], 'R':[0, 1], 'D':[1, 0]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        newhead_i = self.snake[-1][0] + self.direct[direction][0]
        newhead_j = self.snake[-1][1] + self.direct[direction][1]
        
        if not (0 <= newhead_i < self.m and 0 <= newhead_j < self.n) or [newhead_i, newhead_j] in self.snake and [newhead_i, newhead_j] != self.snake[0]:
            # game over
            # especially, when snake hit its tail it's not over
            return -1
        
        elif self.food and self.food[0] == [newhead_i, newhead_j]:
            # eat the food
            self.snake.append([newhead_i, newhead_j]) # add length
            self.food.popleft()
        
        else:
            # just normal moving
            self.snake.popleft()
            self.snake.append([newhead_i, newhead_j]) # move ahead
        
        return len(self.snake) - 1
    

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# I spent much time in modifying the board but actually no need to build the board
# 
# Get similar idea from https://leetcode.com/problems/design-snake-game/discuss/82681/Straightforward-Python-solution-using-deque
# Using deque in python
# 
# Check whether next position hit the body of snake cost O(N) time, N is body length