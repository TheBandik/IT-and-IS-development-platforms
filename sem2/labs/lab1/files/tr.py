import PySide6.QtWidgets as psqw
import PySide6.QtCore as psqc


class MainWindow(psqw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вид треугольника')
        self.setFixedSize(300, 400)
        self.setMinimumSize(10, 10)

        layout = psqw.QVBoxLayout()

        widget = psqw.QWidget()
        widget.setLayout(layout)

        self.l = psqw.QLabel()

        self.a = psqw.QLineEdit()
        self.a.setPlaceholderText("A")

        self.b = psqw.QLineEdit()
        self.b.setPlaceholderText("B")

        self.c = psqw.QLineEdit()
        self.c.setPlaceholderText("C")

        button = psqw.QPushButton('Проверить')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        layout.addWidget(self.l)
        layout.addWidget(self.a)
        layout.addWidget(self.b)
        layout.addWidget(self.c)
        layout.addWidget(button)

        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        try: 
            a = int(self.a.text())
            b = int(self.b.text())
            if self.c.text():
                c = int(self.c.text())
            else:
                c = 3

            if (a == b == c):
                self.l.setText('Равносторонний треугольник')
            if ((a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2)):
                self.l.setText('Прямоугольный треугольник')
            elif ((a == b) or (b == c)):
                self.l.setText('Равнобедренный треугольник')
            elif ((a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2) or (c ** 2 > a ** 2 + b ** 2)):
                self.l.setText('Тупоугольный треугольник')
            elif ((a ** 2 < b ** 2 + c ** 2) or (b ** 2 < a ** 2 + c ** 2) or (c ** 2 < a ** 2 + b ** 2)):
                self.l.setText('Остроугольный треугольник')
            else:
                self.l.setText('Не существует')
        except:
            self.l.setText('Не треугольник')

app = psqw.QApplication()
window = MainWindow()
window.show()
app.exec()
