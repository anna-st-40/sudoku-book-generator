import os

from functions import *
from drawing import draw_page

# Get number of each puzzle 
num_each_puzzle = valid_input("How many puzzles of each difficulty level: ")
input(f"{num_each_puzzle*4} puzzles will be made total. Press any key to confirm")
print()

# Generate a timestamp for the base puzzle id
base_id = timestamp_id()

# Generate all puzzles
os.makedirs(os.path.join(f"sudoku_{base_id}", "puzzles")) #make a folder for the puzzles

print("Generating easy puzzles...")
generate_puzzles(num_each_puzzle, "easy", base_id, page_start=1)
print(f"{num_each_puzzle} easy puzzles generated")

print("Generating medium puzzles...")
generate_puzzles(num_each_puzzle, "medium", base_id, page_start=1+num_each_puzzle)
print(f"{num_each_puzzle} medium puzzles generated")

print("Generating hard puzzles...")
generate_puzzles(num_each_puzzle, "hard", base_id, page_start=1+2*num_each_puzzle)
print(f"{num_each_puzzle} hard puzzles generated")

print("Generating extreme puzzles...")
generate_puzzles(num_each_puzzle, "extreme", base_id, page_start=1+3*num_each_puzzle)
print(f"{num_each_puzzle} extreme puzzles generated")

print("All puzzles generated.\n\n")


# Generate all puzzle pages
print("Generating puzzle pages...")

os.mkdir(f"sudoku_{base_id}\pages") #make a folder for the pages
for filename in [f for f in os.listdir(f"sudoku_{base_id}\puzzles") if os.path.isfile(os.path.join(f"sudoku_{base_id}\puzzles", f))]: #iterate through all the files in the folder
    generate_puzzle_page(filename, base_id)

print("All puzzle pages generated.\n")


# Generate all solution pages
print("Generating solution pages...")
generate_solution_pages(base_id)
print("All solution pages generated.\n")