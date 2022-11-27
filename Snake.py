import turtle
import time
import random

delay = 0.1

# Wynik
score = 0
high_score = 0

# Ekran
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0) # Turns off the screen updates

# Wąż
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

# Jedzenie
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Napis
results = turtle.Turtle()
results.speed(0)
results.shape("square")
results.color("green")
results.penup()
results.hideturtle()
results.goto(0, 260)
results.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "bold"))

# Funkcje
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Przypisanie klawiszy

screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.listen()

# Pętla gry
while True:
    screen.update()

    # Sprawdzenie czy nie dotyka granicy
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        # Usunięcie segmentów poza pole gry
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Wyczyszczenie segmentów
        segments.clear()

        # Reset wyniku
        score = 0

        # Reset opóźnienia
        delay = 0.1

        #reset wyników
        results.clear()
        results.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold")) 


    # sprawdzanie czy dotyka jedzenia
    if snake.distance(food) < 20:
        # przeniesienie jedzenia w losowe miejsce
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # dodanie segmentu
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # uproszczenie kierowania wężem
        delay -= 0.001

        # zwiekszenie wyniku
        score += 10

        if score > high_score:
            high_score = score
        
        results.clear()
        results.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold")) 

    # Przesuń najpierw segmenty końcowe w odwrotnej kolejności
    for index in range(len(segments)-1, 0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Przesunąć segment 0 do miejsca, w którym znajduje się głowa
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            results.clear()
            results.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "bold"))

    time.sleep(delay)
screen.mainloop()