from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout , QComboBox
import sys

class avgspcal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance :")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])
          
        
        calculate_button = QPushButton("Calculate Average Speed")
        calculate_button.clicked.connect(self.calculate_avg_speed)
        self.output=QLabel("")

        # add widgets to layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo,0,2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_avg_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        avg_speed = distance / time

        if self.unit_combo.currentText() == 'Metric (km)':
            speed = round(avg_speed, 2)
            unit = 'km/h'
        if self.unit_combo.currentText() == 'Imperial (miles)':
            speed = round(avg_speed * 0.621371, 2)
            unit = 'mph'
        self.output.setText(f"Average Speed: {speed} {unit}")

app = QApplication(sys.argv)
avg_speed_calculator = avgspcal()
avg_speed_calculator.show()
sys.exit(app.exec())