from PIL import ImageDraw

class SudokuGrid:
    def __init__(self, box_left, box_top, box_width, box_height):
        self.box_left = box_left
        self.box_top = box_top
        self.box_width = box_width
        self.box_height = box_height

    def _textsize(self, font, text):
        left, top, right, bottom = font.getbbox(text)
        width = right - left
        height = bottom - top
        return (width, height)

    def _calculate_text_position(self, font, text, left_bound, right_bound, upper_bound=0, lower_bound=0, y_position="center"):
        """
        Calculates the necessary x and y coordinates to center the text relative to a box.
        y-position values: 'center', 'main title', or 'solution title'
        """

        # Calculate the size of the box
        box_width = abs(right_bound - left_bound)
        box_height = abs(upper_bound - lower_bound)

        # Get the size of the text
        text_width, text_height = self._textsize(font, text)

        # Calculate the coordinate
        x = left_bound + (box_width - text_width) // 2
        if y_position == "center":
            y = upper_bound + (box_height - 2*text_height) // 2
        elif y_position == "main title":
            y = upper_bound - text_height - (2/3)*text_height
        elif y_position == "solution title":
            y = upper_bound - text_height - (1/4)*text_height - 5

        return (x, y)

    def _draw_sudoku_number(self, image, line_color, text, font, left_bound, right_bound, upper_bound, lower_bound):
        draw = ImageDraw.Draw(image)
        text_position = self._calculate_text_position(font, text, left_bound, right_bound, upper_bound, lower_bound)
        draw.text(text_position, text, font=font, fill=line_color)


    def _draw_outer_box(self, image, line_color):
        """Draws the outline of the box."""
        draw = ImageDraw.Draw(image)
        draw.rectangle([(self.box_left, self.box_top), 
                        (self.box_left+self.box_width, self.box_top+self.box_height)], 
                        fill=None, outline=line_color, width=10)
    
    def _draw_outer_grid(self, image, line_color):
        """Draws the heavy-line 3x3 grid inside."""
        draw = ImageDraw.Draw(image)
        
        #Vertical-left
        draw.line([(self.box_left+self.box_width/3, self.box_top), 
                        (self.box_left+self.box_width/3, self.box_top+self.box_height)], 
                        fill=line_color, width=10)
        
        #Vertical-right
        draw.line([(self.box_left+2*self.box_width/3, self.box_top), 
                        (self.box_left+2*self.box_width/3, self.box_top+self.box_height)], 
                        fill=line_color, width=10)
        
        #Horizontal-top
        draw.line([(self.box_left, self.box_top+self.box_height/3), 
                   (self.box_left+self.box_width, self.box_top+self.box_height/3)], 
                   fill=line_color, width=10)
        
        #Horizontal-bottom
        draw.line([(self.box_left, self.box_top+2*self.box_height/3), 
                   (self.box_left+self.box_width, self.box_top+2*self.box_height/3)], 
                   fill=line_color, width=10)
        
    def _draw_inner_grid(self, image, line_color):
        draw = ImageDraw.Draw(image)

        #Left-vertical
        draw.line([(self.box_left+self.box_width/9, self.box_top), 
                    (self.box_left+self.box_width/9, self.box_top+self.box_height)], 
                    fill=line_color, width=5)
        draw.line([(self.box_left+2*self.box_width/9, self.box_top), 
                    (self.box_left+2*self.box_width/9, self.box_top+self.box_height)], 
                    fill=line_color, width=5)
    
        #Center-vertical        
        draw.line([(self.box_left+4*self.box_width/9, self.box_top), 
                   (self.box_left+4*self.box_width/9, self.box_top+self.box_height)], 
                   fill=line_color, width=5)
        draw.line([(self.box_left+5*self.box_width/9, self.box_top), 
                   (self.box_left+5*self.box_width/9, self.box_top+self.box_height)], 
                   fill=line_color, width=5)

        #Right-vertical
        draw.line([(self.box_left+7*self.box_width/9, self.box_top), 
                    (self.box_left+7*self.box_width/9, self.box_top+self.box_height)], 
                    fill=line_color, width=5)
        draw.line([(self.box_left+8*self.box_width/9, self.box_top), 
                    (self.box_left+8*self.box_width/9, self.box_top+self.box_height)], 
                    fill=line_color, width=5)
        
        #Top-horizontal
        draw.line([(self.box_left, self.box_top+self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+self.box_height/9)], 
                    fill=line_color, width=5)
        draw.line([(self.box_left, self.box_top+2*self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+2*self.box_height/9)], 
                    fill=line_color, width=5)
        
        #Center-horizontal
        draw.line([(self.box_left, self.box_top+4*self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+4*self.box_height/9)], 
                    fill=line_color, width=5)
        draw.line([(self.box_left, self.box_top+5*self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+5*self.box_height/9)], 
                    fill=line_color, width=5)
        
        #Bottom-horizontal
        draw.line([(self.box_left, self.box_top+7*self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+7*self.box_height/9)], 
                    fill=line_color, width=5)
        draw.line([(self.box_left, self.box_top+8*self.box_height/9), 
                    (self.box_left+self.box_width, self.box_top+8*self.box_height/9)], 
                    fill=line_color, width=5)


    def draw_grid(self, image, line_color):
        self._draw_outer_box(image, line_color)
        self._draw_outer_grid(image, line_color)
        self._draw_inner_grid(image, line_color)

    def draw_numbers(self, image, line_color, font, nums:list):

        # Determine the size of smallest boxes
        small_box_height = self.box_height/9
        small_box_width = self.box_width/9

        # Determine bounds
        vertical_bounds = [
            self.box_left,
            self.box_left+small_box_width,
            self.box_left+2*small_box_width,
            self.box_left+3*small_box_width,
            self.box_left+4*small_box_width,
            self.box_left+5*small_box_width,
            self.box_left+6*small_box_width,
            self.box_left+7*small_box_width,
            self.box_left+8*small_box_width,
            self.box_left+9*small_box_width,
        ]
        horizontal_bounds = [
            self.box_top,
            self.box_top+small_box_height,
            self.box_top+2*small_box_height,
            self.box_top+3*small_box_height,
            self.box_top+4*small_box_height,
            self.box_top+5*small_box_height,
            self.box_top+6*small_box_height,
            self.box_top+7*small_box_height,
            self.box_top+8*small_box_height,
            self.box_top+9*small_box_height,
        ]

        for i in range(9):
            for j in range(9):
                self._draw_sudoku_number(image, line_color, str(nums[i][j]), font, 
                                        left_bound=vertical_bounds[j], 
                                        right_bound=vertical_bounds[j+1], 
                                        upper_bound=horizontal_bounds[i], 
                                        lower_bound=horizontal_bounds[i+1])

    def draw_title(self, image, line_color, font, text, y_position="center"):
        draw = ImageDraw.Draw(image)

        text_position = self._calculate_text_position(font, text, 
                                                      left_bound=self.box_left, 
                                                      right_bound=self.box_left+self.box_width, 
                                                      upper_bound=self.box_top,
                                                      y_position=y_position)

        draw.text(text_position, text, font=font, fill=line_color)