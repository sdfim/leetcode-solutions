# Robot Room Cleaner
# Problem: https://leetcode.com/problems/robot-room-cleaner/
# Solution:

class Robot:
    def move(self):
        pass

    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def clean(self):
        pass

def cleanRoom(robot):
    def go_back():
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()

    def backtrack(cell, d):
        visited.add(cell)
        robot.clean()

        for i in range(4):
            new_d = (d + i) % 4
            new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])

            if new_cell not in visited and robot.move():
                backtrack(new_cell, new_d)
                go_back()

            robot.turnRight()

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    backtrack((0, 0), 0)

if __name__ == "__main__":
    robot = Robot()
    cleanRoom(robot)
