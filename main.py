import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()
cursor.speed("fastest")

score = 0
game_is_on = True
data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title=f"{score} / 50 states guessed", prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        game_is_on = False

    for state in state_names:
        if answer_state.lower() == state.lower() and state not in guessed_states:
            score += 1
            guessed_states.append(state)
            cursor.goto(int(data[data.state == state]["x"]), int(data[data.state == state]["y"]))
            cursor.write(f"{state}")

    if score == 50:
        game_is_on = False

if score < 50:
    # making a csv file with the remaining, non guessed states:
    remaining_states_list = [state for state in state_names if state not in guessed_states]

    remaining_states_dict = {
        "remaining states": remaining_states_list
    }

    remaining_states_dataframe = pandas.DataFrame(remaining_states_dict)
    remaining_states_dataframe.to_csv("remaining_states.csv")

turtle.mainloop()
