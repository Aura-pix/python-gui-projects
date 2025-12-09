# Python PyQt6 Digital Clock

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QFontDatabase, QFont

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__() 
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 200, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 100px;"\
                                        "color: #00FF00; " \
                                        "background-color: black;")
        
        font_id = QFontDatabase.addApplicationFont("C:\\Users\\HOME PC\\Desktop\\Project 1\\digital-7 (mono).ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font= QFont(font_family, 120)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()  # Initial call to set the time immediately

    def update_time(self):
            current_time = QTime.currentTime().toString('hh:mm:ss AP')
            self.time_label.setText(current_time) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())