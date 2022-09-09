from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(-10, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def get_highest_socre(self):
    #     with open('data.txt') as file:
    #         data = file.read()
    #         return int(data)
    #
    # def update_highest_score(self):
    #     with open('data.txt', mode='w') as file:
    #         data = file.write(f'{self.high_score}')
    #         return int(data)
