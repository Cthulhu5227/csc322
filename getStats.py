import os
import subprocess

# Assuming your puzzle files are in a folder named "puzzles"
PUZZLE_FOLDER = "7/a/easy"
for puzzle_file in os.listdir(PUZZLE_FOLDER):
    if puzzle_file.endswith("-puzzle.txt"):
        puzzle_path = os.path.join(PUZZLE_FOLDER, puzzle_file)
        with open(puzzle_path, "r")
