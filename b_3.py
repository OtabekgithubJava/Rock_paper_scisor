import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class RockPaperScissors(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock, Paper, Scissors")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.rock_button = QPushButton("Rock")
        self.rock_button.clicked.connect(lambda: self.play("Rock"))
        self.layout.addWidget(self.rock_button)

        self.paper_button = QPushButton("Paper")
        self.paper_button.clicked.connect(lambda: self.play("Paper"))
        self.layout.addWidget(self.paper_button)

        self.scissors_button = QPushButton("Scissors")
        self.scissors_button.clicked.connect(lambda: self.play("Scissors"))
        self.layout.addWidget(self.scissors_button)

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            self.result_label.setText(f"It's a tie! You both chose {user_choice}.")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.result_label.setText(f"You win! Computer chose {computer_choice}.")
        else:
            self.result_label.setText(f"You lose! Computer chose {computer_choice}.")

def run_app():
    app = QApplication(sys.argv)
    game = RockPaperScissors()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()