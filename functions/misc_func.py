import os
from datetime import datetime

def valid_input(prompt):
    """
    Self-validating input function that forces user input to be an int.
    """
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            print("Invalid input, try again.")

def sudoku_to_list(file):
    """
    Converts the sudoku puzzle text file to two list of lists of numbers.
    First list is the answer key (all numbers). Second list is the puzzle (numbers and blanks).
    """

    answer_list = []
    puzzle_list = []

    with open(file, "r") as infile:
        for i in range(9):
            line = infile.readline()
            line = line.strip()
            line = line.split("|")
            answer_list.append(line)

        infile.readline()

        for i in range(9):
            line = infile.readline()
            line = line.strip("\n")
            line = line.replace("_", " ")
            line = line.split("|")
            puzzle_list.append(line)

    return answer_list, puzzle_list

def timestamp_id():
    """
    Returns a string using the current time (from year to second) that can be used as a timestamp base for an id.
    """
    now = datetime.now()
    timestamp_id = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2) + str(now.hour).zfill(2) + str(now.minute).zfill(2) + str(now.second).zfill(2)
    return timestamp_id

def filename_sorting_key(filename:str):
    """
    Key function for the sort() method to properly sort files 
    based on this project's output file naming conventions.
    """
    page_num = int(filename.split("_")[2].split(".")[0])
    return page_num

def make_solutions_dicts(files_list:list, base_id):
    """Makes a dict representing 6 solutions, to be turned into a page"""

    solutions = {
        'numbers': [],
        "puzzle_nums" : [],
        'difficulties': []
    }

    for file in files_list:
        solutions["numbers"].append(sudoku_to_list(os.path.join(f"sudoku_{base_id}", "puzzles", file))[0])
        solutions["puzzle_nums"].append(file.split("_")[2])
        solutions["difficulties"].append(file.split("_")[3])

    return solutions