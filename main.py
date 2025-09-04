import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800)

data=pandas.read_csv("50_states.csv")
states=data["state"].to_list()
pen=turtle.Turtle()
pen.hideturtle()
pen.penup()

score=0
answers=[]

while len(answers)<50:
    u_answer = screen.textinput(title="Tpe a state", prompt=f"{score}/50 correct").title()
    if u_answer=="Exit":
        missing_states=[state for state in states if state not in answers]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if u_answer in answers:
        continue
    else:
        if u_answer in states:
            state = data[data["state"] == u_answer]
            x_coor = int(state.x.iloc[0])
            y_coor = int(state.y.iloc[0])
            pen.goto(x_coor,y_coor)
            pen.write(u_answer,align="center")
            answers.append(u_answer)
            score=len(answers)



