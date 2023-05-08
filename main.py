import sys
import random


from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.responses = [ "It is certain." , "It is decidedly so." , "Without a doubt." , "Yes definitely." , "You may rely on it." , "As I see it, yes." , "Most likely." , "Outlook good." , "Yes." , "Signs point to yes." , "Reply hazy, try again." , "Ask again later." , "Better not tell you now." , "Cannot predict now." , "Concentrate and ask again." , "Don't count on it." , "My reply is no." , "My sources say no." , "Outlook not so good." , "Very doubtful."]

        print(len(self.responses))
        
        self.ui.startBtn.clicked.connect(self.run)
        
        
    def run(self):
        print("running")
        
        self.input = self.ui.input.toPlainText()
        
        print(self.input)
        
        selection = random.randint(0,len(self.responses))
        
        self.ui.output.setHtml("<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">" + self.responses[selection] + "</span></p></body></html>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())