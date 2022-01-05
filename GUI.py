import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QDialogButtonBox, QFormLayout, QGridLayout, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


app2 = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('BudgetCalculator')
# Msg = QLabel('Welcome to the Budget Calculator', parent=window)
# Msg.move(100,100)

# layout = QGridLayout()
# layout.addWidget(QPushButton(''), 0, 0)
# layout.addWidget(QPushButton(''), 0, 1)
# layout.addWidget(QPushButton(''), 0, 2)
# layout.addWidget(QPushButton(''), 1, 0)
# layout.addWidget(QPushButton(''), 1, 1)
# layout.addWidget(QPushButton(''), 1, 2)
# layout.addWidget(QPushButton(''), 2, 0)
# layout.addWidget(QPushButton(''), 2, 1, 1, 2)
# window.setLayout(layout)
layout = QFormLayout()
layout.addRow('Budget:', QLineEdit())
layout.addRow('Saving%:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())
window.setLayout(layout)
btns = QDialogButtonBox()
btns.setStandardButtons(
    QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
window.setGeometry(100,100,250,250)
window.move(60, 15)
window.show()

sys.exit(app2.exec_())