x = y = 0

while True:
    robot_step = input("Enter robot steps in 'UP 00 or DOWN 00 or LEFT 00 or RIGHT 00' format:")

    if robot_step == "":
        break

    else:
        steps = robot_step.split()
        direc = steps[0]
        dist = int(steps[1])

        if direc == 'UP':
            y = y + dist

        elif direc == 'DOWN':
            y = y - dist
            # print(y, dist)
            # break
        elif direc == 'LEFT':
            x = x + dist

        elif direc == 'RIGHT':
            x = x - dist
            # print(x, dist)
            # break

print("x, y position of robot is: ", x, ',', y, )