import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QIcon

app_icon = "/home/alexsanderprates/Downloads/iconBravo."

class CustomNotification(QWidget):
    def __init__(self, title, message, app_icon):
        super().__init__()

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(app_icon))
        self.setGeometry(100, 100, 400, 100)

        layout = QVBoxLayout()
        self.label = QLabel(message)
        layout.addWidget(self.label)

        self.close_button = QPushButton("Fechar")
        self.close_button.clicked.connect(self.close_notification)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def close_notification(self):
        self.close()



def show_notification(title, message, app_icon):
    app = QApplication(sys.argv)
    notification = CustomNotification(title, message, app_icon)
    notification.show()
    app.exec_()
