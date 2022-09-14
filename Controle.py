
from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = Formulario.lineEdit.text()
    print ('Cadastro:', linha1)
    linha2 = Formulario.lineEdit_2.text()
    print ('Descrição:', linha2)
    linha3 = Formulario.lineEdit_3.text()
    print ('Preço:', linha3)

    if  Formulario.radioButton.isChecked():
        print('Categoria selecionada  foi Informatica')
    elif Formulario.radioButton_2.ischecked() :
        print('Categoria selecionada foi Alimentos')

app = QtWidgets.QApplication([])
Formulario= uic.loadUi('Formulario.ui')
Formulario.pushButton.clicked.connect(funcao_principal)

Formulario.show()
app.exec()