import turtle
import math
elan=turtle.Screen()
elan.bgcolor('Black')
elan.title("Maze Runner")
elan.setup(700,700)

turtle.register_shape("Wizard")

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Blue")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        if(move_to_x,move_to_y) not in walls:
         self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self,other):
      a=self.xcor()-other.xcor()
      b=self.ycor()-other.ycor()
      distance = math.sqrt((a**2) + (b**2))
      if distance<5:
        return True
      else:
        return False


class Treasure(turtle.Turtle):
    def __init__(self,x,y):
     turtle.Turtle.__init__(self)
     self.shape("circle")
     self.color("gold")
     self.penup()
     self.speed(0)
     self.gold=100
     self.goto(x,y)


    def destroy(self):
       self.goto(2000, 2000)
       self.hideturtle()



levels=[""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXP   XXX  XXXX   XXX  X",
    "XXXX               XXXXXX",
    "X    XXXXXXXXXXX   XXXXXX",
    "XXXXX XXXXX X      T XXXXX",
    "X       XXXXXXXXXXX XX  X",
    "XXXXXXXXXXX             X",
    "X                 XXXXXXX",
    "XXXX        XXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXX      X",
    "XXXXX XXXXX X       XXXXX",
    "X       XXXXXXXXXXX XX  X",
    "XXXXXXXXXXX             X",
    "X                 XXXXXXX",
    "X                 XXXXXXX",
    "XXXX        XXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXXXXXXX",
    "X                 XXXXXXX",
    "XXXX        XXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXXXXXXX",
    "X                 XXXXXXX",
    "XXXX        XXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXX      X",

]

treasures = []
levels.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character=="T":
                treasures.append(Treasure(screen_x,screen_y))





pen=Pen()
player=Player()
walls= []

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")





setup_maze(levels[1])


elan.tracer(0)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold+=treasure.gold
            print("Payer Gold: {}".format(player.gold))

            treasure.destroy()

            treasures.remove(treasure)

    elan.update()
