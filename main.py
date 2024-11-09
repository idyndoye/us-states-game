import turtle
import pandas as pd


from django.template.defaultfilters import title

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:

    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State correct",
                                    prompt="what's another state name?").title()
    # print(answer_state)

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guess_state]

        # missing_state = []
        # for state in all_states:
        #     if state not in guess_state:
        #         missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_learn")
        break





#programme pour avoir le coordonnees sur l'ecran
# def get_coordonnees(x,y):
#     print(x, y)
# turtle.onclick(get_coordonnees) # reçevoir les coordonéés dans une image
# turtle.mainloop() #to keep the screen on clic once until the program finish.
