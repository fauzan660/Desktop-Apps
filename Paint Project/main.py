from shapes import Square, Rectangle
from canvas import Canvas


canvas_width = int(input("Height of canvas: "))
canvas_height = int(input("Width of canvas: "))
canvas_color = input("Color of canvas (tuple value): ")

red, green, blue = map(int, canvas_color.split())
canvas_color = (red, green, blue)

canvas1 = Canvas(color=canvas_color, height=canvas_height, width=canvas_width)  # Increased resolution

while True:
    choice = input("Do you want to make a rectangle or square?: ")
    if choice == "rectangle":
        rect_x = int(input("What should the x coordinate of top left hand corner of the rectangle be: "))
        rect_y = int(input("What should the y coordinate of top left hand corner of the rectangle be: "))
        rect_w = int(input("What should the width of the rectangle be: "))
        rect_h = int(input("What should the height of the rectangle be: "))
        rect_c = input("What should the color of the rectangle be (RGB values only!): ")

        rd, gren, blu = map(int, rect_c.split())
        color_tuple = (rd, gren, blu)

        rect1 = Rectangle(x=rect_x, y=rect_y, width=rect_w, height=rect_h, color=color_tuple)  # Adjusted position and size
        rect1.draw(canvas1)

        canvas1.make("canva.png")

    elif choice == "square":
        sqr_x = int(input("What should the x coordinate of top left hand corner of the rectangle be: "))
        sqr_y = int(input("What should the y coordinate of top left hand corner of the rectangle be: "))
        sqr_s = int(input("What should be length of 1 side of square: "))
        sqr_c = input("What should the color of the rectangle be (RGB values only!): ")

        rd, gren, blu = map(int, sqr_c.split())
        color_tuple = (rd, gren, blu)

        sqr1 = Square(x=sqr_x, y=sqr_y, side= sqr_s, color=color_tuple)  # Adjusted position and size
        sqr1.draw(canvas1)

        canvas1.make("canva.png")


    elif choice == "quit":
        quit()








