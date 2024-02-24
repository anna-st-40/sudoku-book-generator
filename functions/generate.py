import subprocess
import os


from functions.functions import *
from functions.draw import draw_page, draw_solution_page



def generate_sudoku(difficulty, output_folder, output_filename):
    """
    Generates a sudoku puzzle and saves a representation to a text file.
    """

    # Initialize a folder for the generated files
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # Run the sudoku generation script from sudoku-generator repository
    terminal_path = r'C:\Users\Anna\Documents\Programming\Python\My projects\Sudoku Page Generator\sudoku_generator'
    command = f'python sudoku_generation.py base.txt {difficulty}'
    output_path = f"{output_folder}\{output_filename}"
    f = open(output_path, 'w')
    subprocess.run(command, cwd=terminal_path, shell=True, check=True, stdout=f)
    f.close()

    # Format output
    with open(output_path, "r") as infile:
        lines = infile.readlines()
    with open(output_path, "w") as outfile:
        for i, line in enumerate(lines):
            if not i % 2:
                outfile.write(line)

def generate_puzzles(num, difficulty, base_id, page_start):
    """
    Generates a given number of puzzles of a given difficulty and saves them as individual files.
    """
    for i in range(num):
        generate_sudoku(difficulty, output_folder=os.path.join(f"sudoku_{base_id}", "puzzles"), output_filename=f"{base_id}_puzzle_{page_start+i}_{difficulty}")
 
        
def generate_puzzle_page(filename, base_id):
    """Generates a single puzzle page."""

    file_path = os.path.join(f"sudoku_{base_id}\puzzles", filename) # path of puzzle .txt file

    puzzle = sudoku_to_list(file_path)[1] 
    page_num = int(filename.split("_")[2])
    page_side = "right" if page_num % 2 == 1 else "left"
    page_difficulty = filename.split("_")[3]

    draw_page(page_side, page_num, page_difficulty, puzzle, output_folder=f"sudoku_{base_id}\pages", page_filename=f"{base_id}_page_{page_num}_{page_difficulty}")

def generate_solution_page(page_num, relative_page_num, files_list:list, base_id):
    """
    page_num is the numbering in terms of total pages
    relative_page_num is the numbering in terms of solution pages
    """

    solutions = make_solutions_dicts(files_list, base_id)
    page_side = "right" if relative_page_num % 2 == 1 else "left"
    
    draw_solution_page(page_side, solutions, output_folder=f"sudoku_{base_id}\pages", page_filename=f"{base_id}_page_{page_num}_solution")

def generate_solution_pages(base_id):
    files_list = [f for f in os.listdir(f"sudoku_{base_id}/puzzles") if os.path.isfile(os.path.join(f"sudoku_{base_id}/puzzles", f))]
    files_list.sort(key=filename_sorting_key)

    #Generate regular pages
    for i in range(len(files_list)//6):
        generate_solution_page(page_num=(len(files_list)+i+1), relative_page_num=i+1, files_list=files_list[i*6 : 6+i*6], base_id=base_id)

    #Generate leftover page
    if len(files_list) % 6:
        page_start = len(files_list) - (len(files_list) % 6)
        generate_solution_page(page_num=len(files_list)+len(files_list)//6 + 1, relative_page_num=len(files_list)//6 + 1, files_list=files_list[page_start:], base_id=base_id)

