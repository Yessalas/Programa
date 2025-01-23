from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout
import sys
class cadastropatrimonio(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,30,400,300)
################### TITULO ###########################
        self.setWindowTitle("Cadastrar Equipamentos")
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
###################### NOME DO PATRIMÔNIO #################################################
        self.label_patrimonio = QLabel("Nome do patrimônio:")
        self.label_patrimonio.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_patrimonio = QLineEdit()
        self.edit_patrimonio.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## TIPO ################################################
        self.label_tipo = QLabel("Tipo:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## DESCRIÇÃO ################################################
        self.label_descricao = QLabel("Descrição:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## LOCALIZAÇÃO ################################################
        self.label_localizacao = QLabel("Localização:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")
########################## DATA DE FABRICÇÃO ################################################
        self.label_fabricacao = QLabel("Data de fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{background-color:white; padding: 5px;}")
########################## DATA DE AQUISIÇÃO ################################################
        self.label_aquisicao = QLabel("Data de aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt;color:#000}")

        self.edit_aquisicao = QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{ background-color:white; padding: 5px;}")

############################## BOTÃO DE CADASTRAR #######################################################
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:#527ce6; color:white; font-size:12pt; font-weight:bold}")
        # chamando a função cadastar ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

## adicionando a label e o lineedit
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        self.layout_v.addWidget(self.label_patrimonio)
        self.layout_v.addWidget(self.edit_patrimonio)

        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.layout_v.addWidget(self.button)    

## adiciona layout na tela
        self.setLayout(self.layout_v)   
    
    def cadastrar(self):
        arquivo = open("cliente.txt", "+a")
        arquivo.write(f"ID: {self.edit_id.text()}\n")
        arquivo.write(f"Número de série: {self.edit_serie.text()}\n")
        arquivo.write(f"Nome do patrimônio: {self.edit_patrimonio.text()}\n")
        arquivo.write(f"Tipo: {self.edit_tipo.text()}\n")
        arquivo.write(f"Descrição: {self.edit_descricao.text()}\n")
        arquivo.write(f"Localização: {self.edit_localizacao.text()}\n")
        arquivo.write(f"Data de fabricação: {self.edit_fabricacao.text()}\n")
        arquivo.write(f"Data de aquisição: {self.edit_aquisicao.text()}\n")
        arquivo.close()

app = QApplication(sys.argv)
tela = cadastropatrimonio()
tela.show()
app.exec()      