from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
import sys
class Atualizar(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,30,400,300)
################### TITULO ###########################
        self.setWindowTitle("Cadastrar localização")
        self.layout_v = QVBoxLayout()
        self.setStyleSheet("background-color:#9b9cb5")
######################### ID ##########################################################
        self.label_id = QLabel("ID:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{ background-color:white ; padding: 5px;}")
################### NÚMERO DE SÉRIE #######################################################
        self.label_serie = QLabel("Número de série:")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{background-color:white; padding: 5px;}")
###################### DATA DA ÚLTIMA VERIFICAÇÃO #################################################
        self.label_verificacao = QLabel("Data da última verificação:")
        self.label_verificacao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_verificacao = QLineEdit()
        self.edit_verificacao.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## OBSERVAÇÃO ################################################
        self.label_observacao = QLabel("Observação:")
        self.label_observacao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_observacao = QLineEdit()
        self.edit_observacao.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")

############################## BOTÃO DE CADASTRAR #######################################################
        self.button = QPushButton("Atualizar")
        self.button.setStyleSheet("QPushButton{background-color:#527ce6; color:white; font-size:12pt; font-weight:bold}")
        # chamando a função cadastar ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

## adicionando a label e o lineedit
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_verificacao)
        self.layout_v.addWidget(self.edit_verificacao)

        self.layout_v.addWidget(self.label_observacao)
        self.layout_v.addWidget(self.edit_observacao)

        self.layout_v.addWidget(self.button)    

## adiciona layout na tela
        self.setLayout(self.layout_v)   
    
    def cadastrar(self):
        arquivo = open("atualizacao.txt", "+a")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa: {self.edit_serie.text()}\n")
        arquivo.write(f"Logradouro: {self.edit_verificacao.text()}\n")
        arquivo.write(f"Número: {self.edit_observacao.text()}\n")
        arquivo.close()

# app = QApplication(sys.argv)
# tela = Atualizar()
# tela.show()
# app.exec()      