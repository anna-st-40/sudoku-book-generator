from PIL import Image, ImageFont
from functions.sudoku_grid import SudokuGrid


def draw_sudoku_box(image, line_color, side, font, nums:list, title):
    """
    Draws the main puzzle box, its numbers, and its title.
    """
    # Determine margin
    inner_margin = 165
    outer_margin = 125
    left_margin = inner_margin if side == "right" else outer_margin

    # Draw grid using SudokuGrid class
    grid = SudokuGrid(left_margin, 595, 1510, 1510)
    grid.draw_grid(image, line_color)
    grid.draw_numbers(image, line_color, font, nums)
    grid.draw_title(image, line_color, font, title, "main title")
            
def draw_solution_boxes(image, line_color, side, font_title, font_nums, solution_dict:dict):
    """
    Draws up to 6 solutions boxes and its numbers and titles.
    """

    # Extract solution data
    solutions = solution_dict["numbers"]
    puzzle_nums = solution_dict["puzzle_nums"]
    titles = [f"puzzle {puzzle_nums[i]} - {diff}" for i, diff in enumerate(solution_dict["difficulties"])]

    # Determine margin
    inner_margin = 150
    outer_margin = 120
    left_margin = inner_margin if side == "right" else outer_margin
    top_margin = 190

    # Parametric dimensions
    box_width = 760
    box_height = 755
    x_distance_between_boxes = 10
    y_distance_between_boxes = 70

    # Draw sudoku boxes with the numbers
    
    grid1 = SudokuGrid(left_margin, top_margin, box_width, box_height)
    grid1.draw_grid(image, line_color)
    grid1.draw_numbers(image, line_color, font_nums, solutions[0])
    grid1.draw_title(image, line_color, font_title, titles[0], "solution title")

    if len(solutions) >= 2:
        grid2 = SudokuGrid(left_margin+box_width+x_distance_between_boxes, top_margin, box_width, box_height)
        grid2.draw_grid(image, line_color)
        grid2.draw_numbers(image, line_color, font_nums, solutions[1])
        grid2.draw_title(image, line_color, font_title, titles[1], "solution title")

    if len(solutions) >= 3:
        grid3 = SudokuGrid(left_margin, top_margin+box_height+y_distance_between_boxes, box_width, box_height)
        grid3.draw_grid(image, line_color)
        grid3.draw_numbers(image, line_color, font_nums, solutions[2])
        grid3.draw_title(image, line_color, font_title, titles[2], "solution title")

    if len(solutions) >= 4:
        grid4 = SudokuGrid(left_margin+box_width+x_distance_between_boxes, top_margin+box_height+y_distance_between_boxes, box_width, box_height)
        grid4.draw_grid(image, line_color)
        grid4.draw_numbers(image, line_color, font_nums, solutions[3])
        grid4.draw_title(image, line_color, font_title, titles[3], "solution title")

    if len(solutions) >= 5:
        grid5 = SudokuGrid(left_margin, top_margin+2*box_height+2*y_distance_between_boxes, box_width, box_height)
        grid5.draw_grid(image, line_color)
        grid5.draw_numbers(image, line_color, font_nums, solutions[4])
        grid5.draw_title(image, line_color, font_title, titles[4], "solution title")

    if len(solutions) >= 6:
        grid6 = SudokuGrid(left_margin+box_width+x_distance_between_boxes, top_margin+2*box_height+2*y_distance_between_boxes, box_width, box_height)
        grid6.draw_grid(image, line_color)
        grid6.draw_numbers(image, line_color, font_nums, solutions[5])
        grid6.draw_title(image, line_color, font_title, titles[5], "solution title")


# Functions to draw the entire pages
            
def draw_page(side, puzzle_num, difficulty, nums:list, output_folder, page_filename):
    """
    Generates and saves one main puzzle page.
    """
    line_color = "#5d5c5b"
    page_color = "#ffffff"
    font_kawoszeh = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 120)

    new_image = Image.new(mode="RGB", size=(1800, 2700), color=page_color)

    draw_sudoku_box(new_image, line_color, side, font_kawoszeh, nums, f"puzzle {puzzle_num} - {difficulty}")

    new_image.save(f"{output_folder}\{page_filename}.png")

def draw_solution_page(side, solutions:dict, output_folder, page_filename):
    """
    Generates and saves one solution page.
    """
    line_color = "#5d5c5b"
    page_color = "#ffffff"
    font_kawoszeh_title = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 50)
    font_kawoszeh_nums = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 40)

    new_image = Image.new(mode="RGB", size=(1800, 2700), color=page_color)

    draw_solution_boxes(new_image, line_color, side, font_kawoszeh_title, font_kawoszeh_nums, solutions)

    new_image.save(f"{output_folder}\{page_filename}.png")


# Functions to preview pages for testing

def draw_page_preview(side):
    line_color = "#5d5c5b"
    page_color = "#ffffff"
    font_kawoszeh = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 120)

    test_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    new_image = Image.new(mode="RGB", size=(1800, 2700), color=page_color)

    draw_sudoku_box(new_image, line_color, side, font_kawoszeh, test_list, f"puzzle 1 - test")

    new_image.show()

def draw_solution_page_preview(side):
    line_color = "#5d5c5b"
    page_color = "#ffffff"
    font_kawoszeh_title = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 50)
    font_kawoszeh_nums = ImageFont.truetype(r"resources\fonts\kawoszeh\kawoszeh.ttf", 40)

    new_image = Image.new(mode="RGB", size=(1800, 2700), color=page_color)

    test_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    test_solution_list = []
    for i in range(6):
        test_solution_list.append(test_list)

    test_solution_dict = {
        'numbers': test_solution_list,
        "puzzle_nums" : [1, 2, 3, 4, 5, 6],
        'difficulties': ["test" for i in range(6)]
    }

    draw_solution_boxes(new_image, line_color, side, font_kawoszeh_title, font_kawoszeh_nums, test_solution_dict)

    new_image.show()

if __name__ == "__main__":
    #draw_solution_page_preview("left")
    #draw_page_preview("left")
    pass