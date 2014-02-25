import random


def sort_flag(size):
    flag = [random.choice(['r','w','b']) for i in range(size)]

    red = -1             #index of highest red element in red group
    white = -1           #index of highest white element in white group
    blue = len(flag)     #index of lowest blue element in blue group

    while blue > white + 1:
        if flag[white + 1] == 'w':
            white += 1
        elif flag[white + 1] == 'r':
            temp = flag[white + 1]
            flag[white + 1] = flag[red + 1]
            flag[red + 1] = temp
            white += 1
            red += 1
        elif flag[white + 1] == 'b':
            temp = flag[white + 1]
            flag[white + 1] = flag[blue -1]
            flag[blue - 1] = temp
            blue -= 1

    return flag

def main():
    print sort_flag(8)

main()