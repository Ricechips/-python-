'''
Function:
    知乎段子浏览
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import os
import sys
import random
import pickle
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


'''demo'''
class JokeDemo(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(JokeDemo, self).__init__(parent)
        self.all_jokes = self.load()
        # 定义组件
        self.setWindowTitle('黄段子')
        self.setWindowIcon(QIcon('data/icon.png'))
        self.setFixedSize(600, 400)
        self.label_result = QLabel('摘下耳机，我只不过是个落魄的哑巴:')
        self.button_generate = QPushButton('不要点我')
        self.text_result = QTextEdit()
        # 布局
        self.grid = QGridLayout()
        self.grid.addWidget(self.label_result, 0, 0, 1, 1)
        self.grid.addWidget(self.button_generate, 0, 9, 1, 1)
        self.grid.addWidget(self.text_result, 1, 0, 1, 10)
        self.setLayout(self.grid)
        # 事件绑定
        self.button_generate.clicked.connect(self.generate)
    '''随机读取一个段子'''
    def generate(self):
        self.text_result.setText(random.choice(self.all_jokes))
    '''导入所有段子'''
    def load(self):
        root_dir = 'data'
        all_jokes = []
        for item in os.listdir(root_dir):
            if not item.endswith('.pkl'): continue
            with open(os.path.join(root_dir, item), 'rb') as fp:
                joke = pickle.load(fp)
                all_jokes += joke
        return all_jokes


'''run'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = JokeDemo()
    client.show()
    sys.exit(app.exec_())