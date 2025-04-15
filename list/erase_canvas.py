# Import required modules
from graphics import Canvas
import time 

# Define canvas dimensions
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400

# Define size constants
CELL_SIZE: int = 40  # Size of each grid cell
ERASER_SIZE: int = 20  # Size of eraser tool

def erase_objects(canvas, eraser):
    """
    Erases objects that overlap with the eraser by changing their color to white
    Args:
        canvas: The Canvas object to erase from
        eraser: The eraser object to avoid erasing
    """
    # Get current mouse position
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    # Calculate eraser bounds
    left_x = mouse_x
    top_y = mouse_y
    right_x = mouse_x + ERASER_SIZE
    bottom_y = mouse_y + ERASER_SIZE

    # Find and erase overlapping objects
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, "white")

def main():
    # Create canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Calculate grid dimensions
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    # Create grid of blue rectangles
    for row in range(num_rows):
        for col in range(num_cols):
            # Calculate rectangle bounds
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')

    # Wait for user to click to start erasing
    canvas.wait_for_click()

    # Get click position
    last_click_x, last_click_y = canvas.get_last_click()

    # Create pink eraser rectangle
    eraser = canvas.create_rectangle(last_click_x, last_click_y, last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE, 'pink')

    # Main erasing loop
    while True:
        # Get current mouse position
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        # Move eraser to mouse position
        canvas.moveto(eraser, mouse_x, mouse_y)

        # Erase overlapping objects
        erase_objects(canvas, eraser)
        # Small delay to control update rate
        time.sleep(0.05)

if __name__ == "__main__":
    main()