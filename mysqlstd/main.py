from PyQt6.QtWidgets import QApplication,QMessageBox,QStatusBar,\
QMainWindow, QPushButton, QLabel, QToolBar, QGridLayout, QLineEdit,\
QWidget, QTableWidget,QTableWidgetItem ,QDialog,QVBoxLayout, QComboBox
import sys
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction,QIcon
import mysql.connector


class Databaseconnect:
    def __init__(self,host="localhost",user="root",password="15082009",database="student_db"):
        self.host=host
        self.user=user
        self.password=password
        self.database_file=database
        
    def connect(self):
        connecction=mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database_file
        )
        return connecction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("----Student Management System----")
        self.setMinimumSize(800,600)

        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        edit_menu = self.menuBar().addMenu("&Edit")

        add_student = QAction(QIcon("icons/add.png"),"Add Student", self)
        add_student.triggered.connect(self.insert)
        file_menu.addAction(add_student)

        help_action = QAction("Help", self)
        help_menu.addAction(help_action)
        help_action.setMenuRole(QAction.MenuRole.NoRole)

        search = QAction(QIcon("icons/search.png"),"Search Student", self)
        edit_menu.addAction(search)
        search.triggered.connect(self.search)
        

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student)
        toolbar.addAction(search)


        self.statusbar=QStatusBar()
        self.setStatusBar(self.statusbar)

        
        
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children=self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)



    
    def loaddata(self):
        connection = Databaseconnect().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        results = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        cursor.close()
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()
    

    def edit(self):
        dialog = Editdialog()
        dialog.exec()

    def delete(self):
        dialog=Deletedialog()
        dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("insert student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name=QComboBox()
        courses=["Biology","Physis","Astronomy","Math"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course=self.course_name.itemText(self.course_name.currentIndex())
        mobile=self.mobile.text()

        connection = Databaseconnect().connect()
        cursor=connection.cursor()
        cursor.execute("INSERT INTO students (name,course,mobile) VALUES (%s,%s,%s)",
                       (name,course,mobile))
        
        connection.commit()
        cursor.close()
        connection.close()

        window.loaddata()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search  student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Search student")
        layout.addWidget(self.student_name)

        srh_button=QPushButton("Search")
        srh_button.clicked.connect(self.search_student)
        layout.addWidget(srh_button)

        self.setLayout(layout)

    def search_student(self):
        name = self.student_name.text()
        connection = Databaseconnect().connect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        cursor.fetchall()
        row = list(result)[0]
        print(row)
        items = window.table.findItems("John Smith", Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            window.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()
        

class Editdialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("update student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        index = window.table.currentRow()
        student_name=window.table.item(index, 1).text()
        self.student_id=window.table.item(index, 0).text()


        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        course_name = window.table.item(index, 2).text()
        self.course_name=QComboBox()
        courses=["Biology","Physis","Astronomy","Math"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        mobile = window.table.item(index, 3).text()
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Submit")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        connection = Databaseconnect().connect()
        cursor=connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
                       (self.student_name.text(),self.course_name.itemText(self.course_name.currentIndex()),
                        self.mobile.text(),self.student_id))
        
        connection.commit()
        cursor.close()
        connection.close()
        window.loaddata()


class Deletedialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        layout = QGridLayout()

        conformation=QLabel("Are you sure you want to delete ?")
        Yes = QPushButton("yes")
        no = QPushButton("no")

        layout.addWidget(conformation,0,0,1,2)
        layout.addWidget(Yes,1,0)
        layout.addWidget(no,1,1)
        self.setLayout(layout)

        Yes.clicked.connect(self.delete_student)

    def delete_student(self):
        index = window.table.currentRow()
        student_id= window.table.item(index,0).text()

        connection = Databaseconnect().connect()
        cursor=connection.cursor()
        cursor.execute("DELETE from students WHERE id=%s",(student_id,))    
        connection.commit()
        cursor.close()
        connection.close()
        window.loaddata()

        self.close()

        conformation_w=QMessageBox()
        conformation_w.setWindowTitle("Deleted :)")
        conformation_w.setText("The record is delete successfully")
        conformation_w.exec()
         


app = QApplication(sys.argv)
window = MainWindow()
window.show()
window.loaddata()
sys.exit(app.exec())

