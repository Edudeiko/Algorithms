image_str = [
    "#############################",
    "#                           #",
    "#      #########            #",
    "#     #  #      #           #",
    "#    #  # #     #           #",
    "#    #  # #  ###            #",
    "#    #   #  #        ###    #",
    "#     ##    #        # #    #",
    "#      #####       ### ###  #",
    "#                  #     #  #",
    "#                  ### ###  #",
    "#                    # #    #",
    "#############################",
]


print(len(image_str))

# import sys: sys.exit()  #

image = []

for i in image_str:
    image.append(list(i))

def print_image():
    for i in image:
        print("".join(i))

def floodfill(row, col, char):
    if image[row][col] != ' ':
        return

    image[row][col] = char

    floodfill(row, col + 1, char)
    floodfill(row, col - 1, char)
    floodfill(row + 1, col, char)
    floodfill(row - 1, col, char)

floodfill(2, 2, '.')
floodfill(4, 7, '*')


print_image()