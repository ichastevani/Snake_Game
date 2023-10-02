import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=300, height=300, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0

        self.bind_keys()
        self.update_game()

    def bind_keys(self):
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)

    def create_food(self):
        while True:
            x = random.randint(0, 29) * 10
            y = random.randint(0, 29) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + 10, head[1])
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.food = self.create_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if (
            head[0] < 0
            or head[0] >= 300
            or head[1] < 0
            or head[1] >= 300
            or head in self.snake[1:]
        ):
            return True
        return False

    def update_game(self):
        if not self.check_collision():
            self.move()
            self.draw_snake()
            self.draw_food()
            self.root.after(100, self.update_game)
        else:
            self.canvas.create_text(
                150, 150, text=f"Game Over\nScore: {self.score}", fill="red", font=("Helvetica", 20)
            )

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + 10,
                segment[1] + 10,
                fill="green",
                outline="black",
                tags="snake",
            )

    def draw_food(self):
        self.canvas.delete("food")
        self.canvas.create_oval(
            self.food[0],
            self.food[1],
            self.food[0] + 10,
            self.food[1] + 10,
            fill="red",
            outline="black",
            tags="food",
        )

    def move_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"

    def move_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"

    def move_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"

    def move_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
