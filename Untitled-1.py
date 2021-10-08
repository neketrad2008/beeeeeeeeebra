from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определить победителя')
Button = QPushButton('Сгенерировать')
text = QLabel('Нажми, что бы узнать победителя')
winner = QLabel('?')
def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')
Button.clicked.connect(show_winner)
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(Button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
main_win.show()
app.exec_()