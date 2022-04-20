

def draw_hollow_square(char_to_draw, size):
    for i in range(1, size+1):
        for j in range(1, size+1):
            if i == 1 or i == size or j == 1 or j == size:
                print(char_to_draw+" ", end="")
            else:
                print("  ", end="")

        print()


draw_hollow_square(char_to_draw="m", size=7)
