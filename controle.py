from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

conexao = mysql.connector.connect(

    host ='127.0.0.1',
    user = 'root',
    password = '',
    database = 'cadastro_documentos'
)

numero_id = 0

def excluir():
    dadosExcluir = lista.tableWidget.currentRow()
    lista.tableWidget.removeRow(dadosExcluir) # remove a linha selecionada da tela lista
    cursor = conexao.cursor()
    cursor.execute('SELECT id from documentos')
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dadosExcluir] [0]
    cursor.execute('DELETE from documentos WHERE id='+str(valor_id))

    conexao.commit() 

def editar():

    global numero_id
    dados = lista.tableWidget.currentRow()#para identificar a linha 
    cursor = conexao.cursor() #executar um sql no python
    cursor.execute('SELECT id from documentos') #executar um sql dentro do cursor
    leitura_banco = cursor.fetchall()
    valor_id = leitura_banco [dados] [0]
    cursor.execute('SELECT * from documentos WHERE id='+str(valor_id))
    leitura_banco = cursor.fetchall()
    editar.show()

    numero_id = valor_id

    editar.txtAlterarId.setText(str(leitura_banco[0][0]))
    editar.txtAlterarCodigo.setText(str(leitura_banco[0][1]))
    editar.txtAlterarTitulo.setText(str(leitura_banco[0][2]))
    editar.txtAlterarRevisao.setText(str(leitura_banco[0][3]))
    editar.txtAlterarMotivo.setText(str(leitura_banco[0][4]))

    

    

def confirmar_dados():
    global numero_id

    id = editar.txtAlterarId.text()
    codigo = editar.txtAlterarCodigo.text()
    titulo = editar.txtAlterarTitulo.text()
    revisao = editar.txtAlterarRevisao.text()
    motivo = editar.txtAlterarMotivo.text()

    cursor = conexao.cursor()
    cursor.execute("UPDATE documentos SET id='{}', codigo='{}', titulo='{}', revisao='{}', motivo='{}' WHERE id={}".format(id, codigo,titulo,revisao,motivo, numero_id))#para alterar texto existente utilizo '{}'

    editar.close()
    lista.close()
    formulario.show()
    
    conexao.commit()

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle('Alteração')
    msg.setText('Alteração Realizada com Sucesso')
    msg.exec_()

def lista():
    lista.show()
    cursor = conexao.cursor()
    comando_SQL = 'SELECT * FROM documentos'
    cursor.execute(comando_SQL)
    leitura_banco = cursor.fetchall()
    lista.tableWidget.setRowCount(len(leitura_banco))
    lista.tableWidget.setColumnCount(5)

    for i in range(0, len(leitura_banco)):
        for j in range(0,5):
            lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))


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
formulario.btnRelatorio.clicked.connect(lista)
lista=uic.loadUi('lista.ui')
lista.btnAlterar.clicked.connect(editar)
lista.btnDeletar.clicked.connect(excluir)
editar=uic.loadUi('editar.ui')
editar.btnConfirmar.clicked.connect(confirmar_dados)

formulario.show()
app.exec()




















































































































# from PyQt5 import uic, QtWidgets
# from PyQt5.QtWidgets import QMessageBox
# import mysql.connector

# conexao = mysql.connector.connect(

#     host ='127.0.0.1',
#     user = 'root',
#     password = '',
#     database = 'cadastro_documentos'
# )

# numero_id = 0


# def excluir():
#     dadosExcluir = lista.tableWidget.currentRow()
#     lista.tableWidget.removeRow(dadosExcluir) # remove a linha selecionada da tela lista
#     cursor = conexao.cursor()
#     cursor.execute('SELECT id from documentos')
#     leitura_banco = cursor.fetchall()
#     valor_id = leitura_banco [dadosExcluir] [0]
#     cursor.execute('DELETE from documentos WHERE id='+str(valor_id))

#     conexao.commit() 


# def editar():

#     global numero_id
#     dados = lista.tableWidget.currentRow()#para identificar a linha 
#     cursor = conexao.cursor() #executar um sql no python
#     cursor.execute('SELECT id from documentos') #executar um sql dentro do cursor
#     leitura_banco = cursor.fetchall()
#     valor_id = leitura_banco [dados] [0]
#     cursor.execute('SELECT * from documentos WHERE id='+str(valor_id))
#     leitura_banco = cursor.fetchall()
#     editar.show()

#     numero_id = valor_id

#     editar.txtAlterarId.setText(str(leitura_banco[0][0]))
#     editar.txtAlterarCodigo.setText(str(leitura_banco[0][1]))
#     editar.txtAlterarTitulo.setText(str(leitura_banco[0][2]))
#     editar.txtAlterarRevisao.setText(str(leitura_banco[0][3]))
#     editar.txtAlterarMotivo.setText(str(leitura_banco[0][4]))

    

    


# def confirmar_dados():
#     global numero_id

#     id = editar.txtAlterarId.text()
#     codigo = editar.txtAlterarCodigo.text()
#     titulo = editar.txtAlterarTitulo.text()
#     revisao = editar.txtAlterarRevisao.text()
#     motivo = editar.txtAlterarMotivo.text()

#     cursor = conexao.cursor()
#     cursor.execute("UPDATE documentos SET id='{}', codigo='{}', titulo='{}', revisao='{}', motivo='{}' WHERE id={}".format(id, codigo,titulo,revisao,motivo, numero_id))#para alterar texto existente utilizo '{}'

#     editar.close()
#     lista.close()
#     formulario.show()
    
#     conexao.commit()

#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Warning)
#     msg.setWindowTitle('Alteração')
#     msg.setText('Alteração Realizada com Sucesso')
#     msg.exec_()


# def lista():
#     lista.show()
#     cursor = conexao.cursor()
#     comando_SQL = 'SELECT * FROM documentos'
#     cursor.execute(comando_SQL)
#     leitura_banco = cursor.fetchall()
#     lista.tableWidget.setRowCount(len(leitura_banco))
#     lista.tableWidget.setColumnCount(5)

#     for i in range(0, len(leitura_banco)):
#         for j in range(0,5):
#             lista.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_banco[i][j])))



# def inserir():
#     codigo = formulario.txtCodigo.text()
#     titulo = formulario.txtTitulo.text()
#     revisao = formulario.txtRevisao.text()
#     motivo = formulario.txtMotivo.text()

#     cursor = conexao.cursor()
#     comando_SQL = 'INSERT INTO documentos (codigo, titulo, revisao, motivo) VALUES (%s, %s, %s, %s)'
#     dados = (str(codigo), str(titulo), str(revisao), str(motivo))
#     comando_SQL = 'SELECT * FROM documentos WHERE'
#     cursor.execute()
#     leitura_banco = cursor.fetchall()

#     if  dados[1] == leitura_banco[1]:
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Warning)
#         msg.setWindowTitle('Erro de cadastro')
#         msg.setText('Documento Existente')
#         msg.exec_()
#     else:
#         cursor.execute(comando_SQL,dados)
#         conexao.commit()

#     formulario.txtCodigo.setText('')
#     formulario.txtTitulo.setText('')
#     formulario.txtRevisao.setText('')
#     formulario.txtMotivo.setText('')

#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Warning)
#     msg.setWindowTitle('Cadastro')
#     msg.setText('Cadastro Realizado com Sucesso')
#     msg.exec_()

#     consulta_sql = "SELECT * FROM documentos"
#     cursor.execute (consulta_sql)
#     linhas = cursor.fetchall()
#     for linha in linhas:
#         print("Id:", linha[0])
#         print("Código:", linha[1])
#         print("Título:", linha[2])
#         print("Revisão:", linha[3])
#         print("Motivo:", linha[4])




# app=QtWidgets.QApplication([])
# formulario=uic.loadUi('formulario.ui')
# formulario.btnCadastrar.clicked.connect(inserir)
# formulario.btnRelatorio.clicked.connect(lista)
# lista=uic.loadUi('lista.ui')
# lista.btnAlterar.clicked.connect(editar)
# lista.btnDeletar.clicked.connect(excluir)
# editar=uic.loadUi('editar.ui')
# editar.btnConfirmar.clicked.connect(confirmar_dados)


# formulario.show()
# app.exec()




