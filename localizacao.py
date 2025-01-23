from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
import sys
class cadastralocalizacao(QWidget):
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
################### EMPRESA #######################################################
        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{background-color:white; padding: 5px;}")
###################### LOGRADOURO #################################################
        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## NÚMERO ################################################
        self.label_numero = QLabel("Número:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## PRÉDIO ################################################
        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## ANDAR ################################################
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## SALAS ################################################
        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{background-color:white; padding: 5px;}")


############################## BOTÃO DE CADASTRAR #######################################################
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:#527ce6; color:white; font-size:12pt; font-weight:bold}")
        # chamando a função cadastar ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

## adicionando a label e o lineedit
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        self.layout_v.addWidget(self.button)    

## adiciona layout na tela
        self.setLayout(self.layout_v)   
    
    def cadastrar(self):
        arquivo = open("localizacao.txt", "+a")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa: {self.edit_empresa.text()}\n")
        arquivo.write(f"Logradouro: {self.edit_logradouro.text()}\n")
        arquivo.write(f"Número: {self.edit_numero.text()}\n")
        arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
        arquivo.write(f"Andar: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala: {self.edit_sala.text()}\n")
        arquivo.close()

app = QApplication(sys.argv)
tela = cadastralocalizacao()
tela.show()
app.exec()      