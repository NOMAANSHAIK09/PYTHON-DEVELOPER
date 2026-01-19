from PyQt6.QtWidgets import QMainWindow,QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
import sys
from backend import ChatBot
import threading

class Chatbotwindow(QMainWindow):
    def __init__(self): 
        super().__init__()

        self.chatbot = ChatBot()

        self.setWindowTitle("Chatbot")
        self.setMinimumSize(600, 700)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 380, 500)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 520, 300, 30)
        self.input_field.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(320, 520, 70, 30)
        self.send_button.clicked.connect(self.send_message) 

        self.show()


    def send_message(self):
        user_input = self.input_field.text()
        self.chat_area.append(f"You: {user_input}")
        self.input_field.clear()

        thread=threading.Thread(target=self.get_bot_response,args=(user_input,))
        thread.start()
    def get_bot_response(self, user_input):
        
        bot_response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {bot_response}")

        


app = QApplication(sys.argv)
window = Chatbotwindow()
window.show()
sys.exit(app.exec())