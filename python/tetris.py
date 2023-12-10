import turtle
import random
import time

# This dictionary contains the blocks' information
blocks = {
    "I": {
        "color": "cyan",
        "tiles":
            [ [ [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ],
                [ 1, 0, 0, 0 ] ],

              [ [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 0, 0, 0, 0 ],
                [ 1, 1, 1, 1 ] ] ]
    },
    "J": {
        "color": "blue",
        "tiles":
            [ [ [ 0, 1, 0 ],
                [ 0, 1, 0 ],
                [ 1, 1, 0 ] ],

              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 0, 0, 1 ] ],

              [ [ 1, 1, 0 ],
                [ 1, 0, 0 ],
                [ 1, 0, 0 ] ],

              [ [ 0, 0, 0 ],
                [ 1, 0, 0 ],
                [ 1, 1, 1 ] ] ]
    },
    "L": {
        "color": "orange",
        "tiles":
            [ [ [ 1, 0, 0 ],
                [ 1, 0, 0 ],
                [ 1, 1, 0 ] ],

              [ [ 0, 0, 0 ],
                [ 0, 0, 1 ],
                [ 1, 1, 1 ] ],

              [ [ 0, 1, 1 ],
                [ 0, 0, 1 ],
                [ 0, 0, 1 ] ],

              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 1, 0, 0 ] ] ]
    },
    "S": {
        "color": "lime",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 0, 1, 1 ],
                [ 1, 1, 0 ] ],

              [ [ 1, 0, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 0 ] ] ]
    },
    "Z": {
        "color": "red",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 1 ] ],

              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ] ]
    },
    "O": {
        "color": "yellow",
        "tiles": [ [ [ 1, 1 ],
                     [ 1, 1 ] ] ]
    },
    "T": {
        "color": "magenta",
        "tiles":
            [ [ [ 0, 0, 0 ],
                [ 0, 1, 0 ],
                [ 1, 1, 1 ] ],

              [ [ 0, 1, 0 ],
                [ 1, 1, 0 ],
                [ 0, 1, 0 ] ],

              [ [ 0, 0, 0 ],
                [ 1, 1, 1 ],
                [ 0, 1, 0 ] ],

              [ [ 1, 0, 0 ],
                [ 1, 1, 0 ],
                [ 1, 0, 0 ] ] ]
    }
}


# Initialize the map variables
tile_size = 25
map_rows = 20
map_cols = 10
map_x = -125
map_y = 250

# Create the map turtle
map_turtle = turtle.Turtle()
map_turtle.hideturtle()
map_turtle.up()

# Create the game map using a list of lists
game_map = []
for row in range(map_rows):
    game_row = []
    for col in range(map_cols):
        game_row.append("")
    game_map.append(game_row)


# Initialize the block variables
active_block = None
active_block_row = 0
active_block_col = 0
active_block_index = 0
pause = 0

# Create the block turtle
block_turtle = turtle.Turtle()
block_turtle.hideturtle()
block_turtle.up()


# Initialize the game update interval
game_update_interval = 250

# Initialize the game score
score = 0

# Determine if the game is over or not
game_over = False


# This helper function draws a box with the given parameters using the turtle t
def draw_box(t, width, height, pencolor, fillcolor):
    t.color(pencolor, fillcolor)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.up()


# This function draws the game map
def draw_map():
    map_turtle.clear()

    for row in range(map_rows):
        for col in range(map_cols):
            map_turtle.goto(map_x + tile_size * col, map_y - tile_size * row)

            if game_map[row][col] == "":
                draw_box(map_turtle, tile_size, tile_size, "black", "white")
            else:
                block_color = blocks[game_map[row][col]]["color"]
                draw_box(map_turtle, tile_size, tile_size, "black", block_color)



# This function makes a new block to start from the top
def make_new_block():
    global active_block
    global active_block_row, active_block_col
    global active_block_index

    block_types = list(blocks.keys())
    active_block = block_types[random.randint(0, len(block_types)-1)]
    active_block_row = 0
    active_block_col = 4
    active_block_index = 0


# This function draws the active block
def draw_block():
    block_turtle.clear()
    x = map_x + active_block_col * tile_size
    y = map_y - active_block_row * tile_size
    block_color = blocks[active_block]["color"]
    block_tiles = blocks[active_block]["tiles"][active_block_index]
    for row in range(len(block_tiles)):
        for col in range(len(block_tiles[row])):
            if block_tiles[row][col]== 1:
                block_turtle.goto(x + col * tile_size, y - row * tile_size)
                draw_box(block_turtle, tile_size, tile_size, "black", block_color )


# This function tests whether the block is valid given its information
def is_valid_block(block_type, block_row, block_col, block_index):
    block_tiles = blocks[block_type]["tiles"][block_index]

    for row in range(len(block_tiles)):
        for col in range(len(block_tiles[row])):
           if block_tiles[row][col] == 1:
               tile_row = block_row + row
               tile_col = block_col + col
               if tile_row < 0 or tile_row >= map_rows or tile_col < 0 or tile_col >= map_cols:
                   return False

               if game_map[tile_row][tile_col] != "":
                   return False
    return True


# This function sets the active block onto the game map
def set_block_on_map():
    block_tiles = blocks[active_block]["tiles"][active_block_index]
    for row in range(len(block_tiles)):
        for col in range(len(block_tiles[row])):
            if block_tiles[row][col] == 1:
                map_row = row + active_block_row
                map_col = col + active_block_col
                game_map[map_row][map_col] = active_block



# This function removes the completed rows on the map
def remove_completed_rows():
    global game_map
    global game_update_interval
    new_map = []
    for row in range(len(game_map)):
        game_row = game_map[row]
        if "" in game_row:
            new_map.append(game_row)
        else:
            global score
            score = score + 10
            print("Score:", score)
            if score%5 == 0:
                game_update_interval = game_update_interval - 25
    for row in range(0, map_rows - len(new_map)):
        game_row = []
        for col in range(map_cols):
            game_row.append("")
        new_map.insert(0, game_row)
    game_map = new_map


# This function is the game loop which updates in fixed intervals
def game_loop():
    global active_block, active_block_row, pause
    if pause == 0:
        if active_block == None:
            make_new_block()
            if not is_valid_block(active_block, active_block_row, active_block_col, active_block_index):
                return


            draw_block()

        else:
            new_block_row = active_block_row + 1
            if is_valid_block(active_block, new_block_row, active_block_col, active_block_index):
                active_block_row = new_block_row
                draw_block()



            else:
                set_block_on_map()
                remove_completed_rows()
                draw_map()
                active_block = None
    elif pause == 1:
        time.sleep(1)

    turtle.update()
    turtle.ontimer(game_loop, game_update_interval)


# Set up the turtle window
turtle.setup(800, 600)
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Draw the background border around the map
turtle.goto(map_x - 10, map_y + 10)
draw_box(turtle, tile_size * map_cols + 20, tile_size * map_rows + 20, \
         "", "skyblue")

# Draw the empty map in the window
draw_map()
turtle.update()

# Set up the game loop
turtle.ontimer(game_loop, game_update_interval)


# This function handles the rotation of the block
def rotate():
    global active_block_index
    if active_block == None:
        return
    new_block_index = active_block_index + 1
    if new_block_index == len(blocks[active_block]["tiles"]):
      new_block_index = 0
    if is_valid_block(active_block, active_block_row, active_block_col, new_block_index):
        active_block_index = new_block_index
        draw_block()



# This function handles the left movement of the block
def move_left():
    global active_block_col
    if active_block == None:
        return
    new_block_col = active_block_col - 1
    if is_valid_block(active_block, active_block_row, new_block_col, active_block_index):
        active_block_col = new_block_col
        draw_block()


# This function handles the right movement of the block
def move_right():
    global active_block_col
    if active_block == None:
        return
    new_block_col = active_block_col + 1
    if is_valid_block(active_block, active_block_row, new_block_col, active_block_index):
        active_block_col = new_block_col

        draw_block()


# This function drop the block down the map
def drop():
    global active_block_row
    if active_block == None:
        return
    new_block_row = active_block_row + 1
    while is_valid_block(active_block, new_block_row, active_block_col, active_block_index):
        new_block_row = new_block_row + 1
    active_block_row = new_block_row - 1
    draw_block()

# This function changes the block
def change_block():
    global active_block
    block_types = list(blocks.keys())
    active_block = block_types[random.randint(0, len(block_types)-1)]

# This function stops the block
def stop_block():
    global active_block
    global active_block_row
    global pause
    if pause == 0:
        pause += 1
    elif pause == 1:
        pause -= 1




# Set up the key handlers
turtle.onkeypress(rotate, "Up")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(drop, "Down")
turtle.onkeypress(change_block, "c")
turtle.onkeypress(stop_block, "space")


turtle.listen()
turtle.done()
