from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
import sys
from datetime import datetime

class ageCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        self.nameLabel = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_birth = QLabel("Date of Birth (YYYY-MM-DD):")
        self.date_birth= QLineEdit()
        
        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output=QLabel("")


        # add widgets to layout
        grid.addWidget(self.nameLabel, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_birth, 1, 0)
        grid.addWidget(self.date_birth, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        birth_date = self.date_birth.text()
        year_of_birth = datetime.strptime(birth_date, "%Y/%m/%d").date().year
        age = current_year - year_of_birth
        self.output.setText(f"{self.name_line_edit.text()}, you are {age} years old.")

app = QApplication(sys.argv)
age_calculator = ageCalculator()
age_calculator.show()
sys.exit(app.exec())

