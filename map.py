import os
import sys
import termios
import tty

# Terminal settings for capturing key presses
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

# Clear the terminal
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Draw the map with the character
def draw_map(map_data, player_pos):
    clear_screen()
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if (x, y) == player_pos:
                print('@', end='')
            else:
                print(char, end='') 
        print()

# Main game function
def main():
    # Initial map and player position
    map_data = [
        "-----------------",
        "|               |",
        "|               |",
        "|               |",
        "|               |",
        "|               |",
        "|               |",
        "-----------------"
    ]
    player_pos = (1, 1)

    # Game loop
    while True:
        draw_map(map_data, player_pos)
        key = get_key()

        # Move the player based on key input
        if key == 'w' and player_pos[1] > 1:
            player_pos = (player_pos[0], player_pos[1] - 1)
        elif key == 's' and player_pos[1] < len(map_data) - 2:
            player_pos = (player_pos[0], player_pos[1] + 1)
        elif key == 'a' and player_pos[0] > 1:
            player_pos = (player_pos[0] - 1, player_pos[1])
        elif key == 'd' and player_pos[0] < len(map_data[0]) - 2:
            player_pos = (player_pos[0] + 1, player_pos[1])
        elif key == 'q':
            break  # Exit the game loop

if __name__ == "__main__":
    main()
