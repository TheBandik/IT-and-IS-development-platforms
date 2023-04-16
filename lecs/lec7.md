# Лекция №7

## Qt Designer

До сих пор мы создавали приложения с использованием кода Python. Во многих случаях это прекрасно работает, но по мере того, как ваши приложения становятся больше или интерфейсы усложняются, определение всех виджетов программно может стать немного громоздким. Хорошей новостью является то, что Qt поставляется с графическим редактором Qt Designer - который содержит редактор пользовательского интерфейса с возможностью перетаскивания. Используя Qt Designer, вы можете визуально определить свои пользовательские интерфейсы, а затем просто подключить логику приложения позже.

Для того, чтобы запустить Qt Designer необходимо его найти в папке библиотек python.

Примерный путь расположения на Windows, если PySide установлен глобально:

```
C:\Users\thebandik\AppData\Local\Programs\Python\Python310\Lib\site-packages\PySide2
```

Примерный путь расположения, если PySide установлен локально в проекте PyCharm:

```
venv\Lib\site-packages\PySide2
```

Примерный путь расположения на macOS, если PySide установлен глобально:

```
/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/PySide6
```

## Подключение к файла к проекту python

При сохранении вы получите файл с расширением ui, который можно подключить к вашему проекту python. Но удобнее будет конвертировать  формат ui в код python. Для этого в консоли необходимо воспользоваться инструментом pyside2-uic в консоли:

```
pyside2-uic <имя файла ui> -o <имя файла py>
```

Чтобы создать главное окно в вашем приложении, создайте класс как обычно, но в качестве подкласса как из QMainWindow, так и из импортированного класса Ui_MainWindow. Наконец, вызовите self.setupUi(self) из __init__, чтобы инициировать настройку интерфейса.

```
from PySide2 import QtWidgets

from mainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
```

Можно использовать сгенерированный файл, либо написать удобный для себя на основе сгенерированного.

## MVC

https://www.notion.so/thebandik/9-ff5092eb0f0c4ccbac3b20004da3592b

## Упаковка приложений

Библиотека PyInstaller позволяет упаковывать python приложения.

```
pyinstaller myscript.py
```

https://www.notion.so/thebandik/10-d1abc9d987544ea89194c5e5cd8a467e
