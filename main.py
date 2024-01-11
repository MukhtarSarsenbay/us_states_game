import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
data_set = ()
data_set += (data.x, data.y)
to_learn = data_list
turtle.shape(image)
correct_guesses = []
while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{len(correct_guesses)}/50 states correct Guess the State", prompt="What's another state name?").title()
    if answer == "Exit":
        new_file = pandas.DataFrame(to_learn)
        new_file.to_csv("states_to_learn.csv")
        break
    if answer in data_list and answer not in correct_guesses:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        correct_guesses.append(answer)
        to_learn.remove(answer)

