import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed", prompt="Guess the State:").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
