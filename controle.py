from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

conexao = mysql.connector.connect(

    host ='127.0.0.1',
    user = 'root',
    password = '',
    database = 'cadastro_documentos'
)

def inserir():
    codigo = formulario.txtCodigo.text()
    titulo = formulario.txtTitulo.text()
    revisao = formulario.txtRevisao.text()
    motivo = formulario.txtMotivo.text()

    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO documentos (codigo, titulo, revisao, motivo) VALUES (%s, %s, %s, %s)'
    dados = (str(codigo), str(titulo), str(revisao), str(motivo))
    cursor.execute(comando_SQL,dados)
    conexao.commit()

    formulario.txtCodigo.setText('')
    formulario.txtTitulo.setText('')
    formulario.txtRevisao.setText('')
    formulario.txtMotivo.setText('')

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Cadastro')
    msg.setText('Cadastro Realizado com Sucesso')
    msg.exec_()

    consulta_sql = "SELECT * FROM documentos"
    cursor.execute (consulta_sql)
    linhas = cursor.fetchall()
    for linha in linhas:
        print("Id:", linha[0])
        print("Código:", linha[1])
        print("Título:", linha[2])
        print("Revisão:", linha[3])
        print("Motivo:", linha[4])




app=QtWidgets.QApplication([])
formulario=uic.loadUi('formulario.ui')
formulario.btnCadastrar.clicked.connect(inserir)


formulario.show()
app.exec()




