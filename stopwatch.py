# Python PyQt5 StopWatch

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import QTimer, QTime, Qt
# from PyQt6.QtGui import QFontDatabase, QFont

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self) 
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('StopWatch')

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
            }

            QLabel {
                color: #00eaff;
                font-size: 120px;
                background-color: #001f2e;
                border: 3px solid #00eaff;
                border-radius: 25px;
                padding: 20px;
                font-weight: bold;
                qproperty-alignment: AlignCenter;

                /* Neon glow */
                text-shadow: 0 0 20px #00eaff;
            }

            QPushButton {
                background-color: #00141d;
                color: #00eaff;
                font-size: 40px;
                padding: 15px 35px;
                border: 2px solid #00eaff;
                border-radius: 15px;

                /* button glow */
                box-shadow: 0 0 10px #00eaff;
            }

            QPushButton:hover {
                background-color: #003044;
                box-shadow: 0 0 25px #00eaff;
            }

            QPushButton:pressed {
                background-color: #005a80;
                box-shadow: 0 0 10px #00eaff inset;
            }
        """)


        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)  # Update every 10 milliseconds

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))      

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"
    

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec())        