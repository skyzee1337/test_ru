from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, choice
class Quation():
    def __init__(self, q, r_a, w_a1, w_a2, w_a3):
        self.question = q
        self.right_answer = r_a
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3

Quations = []
Quations.append(Quation('кто я?',
                        'ЧИПСЫ ЛИТ ЭНАРГЕ',
                        'медведь',
                        'кот',
                        'утка'))
Quations.append(Quation('коричневое...',
                        'ухо фараона',
                        'чего?',
                        'bad input',
                        'о нееет оно не работает'))
Quations.append(Quation('к тебе приходят исправлять оценку',
                        'сказать что ты занят(играть в косынку)',
                        'выгнать из класса (и играть в косынку)',
                        'поставить еще одну два (и играть в косынку)',
                        'обьеснить тему и дать исправить оценку(шучу. играть в косынку)'))                        
            
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    chinazes.setText('Следующий вопрос')
    print('статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:', main_win.score/main_win.total * 100 ,'%')

def show_quation():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    chinazes.setText('ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_text():
    if chinazes.text() == 'ответить':
        check_answer()
    else: 
        next_quation()



def ask(q:Quation):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    question.setText(q.question)
    wewewew.setText(q.right_answer)
    show_quation()

def check_answer():
    if buttons[0].isChecked():
        wiwiwiw.setText('Правильно')
        main_win.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        wiwiwiw.setText('Неправильно')
        show_result()

def next_quation():
    main_win.total += 1
    rand_q = choice(Quations)
    ask(rand_q)





app = QApplication([])
main_win = QWidget()
main_win.score = 0
main_win.total = 0






question = QLabel('чиназес')
rbtn1 = QRadioButton('жди докс')
rbtn2 = QRadioButton('музыкальная паУза')
rbtn3 = QRadioButton('коричневое ухо фараона китовых барозд')
rbtn4 = QRadioButton('ААААА ЛИТЭНАРГЕ')

buttons =[rbtn1, rbtn2, rbtn3, rbtn4]


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)



AnsGroupBox = QGroupBox('результаты')
AnsGroupBox.hide()
group_v_line1 = QVBoxLayout()
wiwiwiw = QLabel('Правильно/Неправильно')
wewewew = QLabel('Правильный ответ')
group_v_line1.addWidget(wiwiwiw)
group_v_line1.addWidget(wewewew)
AnsGroupBox.setLayout(group_v_line1)

chinazes = QPushButton('ответить')

RadioGroupBox = QGroupBox('варианты')
V_line1 = QVBoxLayout()
V_line2 = QVBoxLayout()
V_line3 = QVBoxLayout()

H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
H_line3 = QHBoxLayout()
H_line4 = QHBoxLayout()

V_line1.addWidget(rbtn1)
V_line1.addWidget(rbtn2)
V_line2.addWidget(rbtn3)
V_line2.addWidget(rbtn4)

H_line1.addLayout(V_line1)
H_line1.addLayout(V_line2)
RadioGroupBox.setLayout(H_line1)

H_line2.addWidget(question)
H_line3.addWidget(RadioGroupBox)
H_line3.addWidget(AnsGroupBox)
H_line4.addWidget(chinazes)

V_line3.addLayout(H_line2)
V_line3.addLayout(H_line3)
V_line3.addLayout(H_line4)

main_win.setLayout(V_line3)













chinazes.clicked.connect(start_text)
main_win.setWindowTitle('Memory Card')
next_quation()
main_win.resize(400, 400)
main_win.show()
app.exec_()