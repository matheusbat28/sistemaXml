import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from tela.tela import Ui_MainWindow

import funcao.funcao as funcao

# classe para a criação da tela 
class TratadoXml(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None): # iniciador das variaveis globais 
        super().__init__(parent)
        super().setupUi(self)
        self.btArquivo.clicked.connect(self.abrirArquivo) # conexão da função como o botão (abrir o arquivo)
        self.btAlterar.clicked.connect(self.alterar) # conexão da função como o botão (alterar o arquivo)
        self.btSalvar.clicked.connect(self.salvar) # conexão da função como o botão (salvar o arquivo)
        self.btLimpar.clicked.connect(self.limpar) # conexão da função como o botão (limpar o campos de escrita)
        self.arquivo = None # variavel para salvar o arquivo xml convertido para string
        self.dados = None # variavel para salvar o arquivo modificado 
        self.urlArquivo = None # variavel para salvar a url do arquivo escolhido

    # função para abrir o arquivo e converter o conteudo para string
    def abrirArquivo(self):
        arquivo = QFileDialog.getOpenFileName()[0] # receber a url do arquivo selecionado
        self.urlArquivo = arquivo

        try:
            with open(arquivo, 'r',encoding= 'UTF-8') as xml: # abre o arquivo
                strXml = str(xml.read()) # converte o arquivo para string
                self.lbArquivo.setText(strXml)
                self.varArquivo.setText(arquivo)
                self.arquivo = strXml

        except FileNotFoundError:
            QMessageBox.critical(self, 'ops!! erro', 'erro ao achar o arquivo')

    # função para alterar o conteudo do arquivo
    def alterar(self):
        if self.arquivo is None: # verifica se o arquivo não estar vazio
            QMessageBox.critical(self, 'ops erro!!',
                                 f'não tem nenhum arquivo para ser alterado')

        else:
            if(self.verificarFormulario()): # verifica se o formulario não estar vazio
                    # faz as alterações para os campos necessario
                    arquivoFinal = funcao.trocarTexto(self.arquivo, '<featureLabel>', '</featureLabel>',
                                                      self.varRamal.text().strip())
                    arquivoFinal = funcao.trocarTexto(
                        arquivoFinal, '<name>', '</name>', self.varRamal.text().strip())
                    arquivoFinal = funcao.trocarTexto(arquivoFinal, '<displayName>', '</displayName>',
                                                      self.varRamal.text().strip())
                    arquivoFinal = funcao.trocarTexto(arquivoFinal, '<authName>', '</authName>',
                                                      self.varRamal.text().strip())
                    arquivoFinal = funcao.trocarTexto(arquivoFinal, '<contact>', '</contact>',
                                                      self.varRamal.text().strip())
                    arquivoFinal = funcao.trocarTexto(arquivoFinal, '<authPassword>', '</authPassword>',
                                                      self.varSenha.text().strip())
                    self.lbArquivo.setText(arquivoFinal)
                    self.limpar()
                    QMessageBox.information(
                        self, 'sucesso', 'documento alterado')
                    self.dados = arquivoFinal # salva o arquivo alterado na variavel global 

    # função para salvar o arquivo no pc
    def salvar(self):
        if self.dados is None: # verifica se o arquivo não foi alterado
            QMessageBox.critical(self, 'ops erro!!',
                                 f'não tem nenhum arquivo alterado para ser salvo')

        elif self.urlArquivo is None: # verifica se o arquivo não estar vazio
            QMessageBox.critical(self, 'ops erro!!',
                                 f'não tem nenhum arquivo para ser apagado')           

        else:
            arquivo = QFileDialog.getSaveFileName()[0] # recebe o novo caminho para salvar o arquivo

            if arquivo == self.urlArquivo: # salva o arquivo caso o novo caminho seja igual o antigo 
                try: 
                    with open(arquivo, 'w') as xml:
                        xml.write(self.dados)
                        self.varArquivo.clear()
                        self.lbArquivo.clear()

                        QMessageBox.information(
                        self, 'salvo como sucesso', f'local do arquivo {arquivo}')
                        
                except FileExistsError:
                    QMessageBox.critical(self, 'ops erro!!',
                                'esse arquivo não existe')
                except FileNotFoundError:
                    QMessageBox.critical(self, 'ops erro!!',
                                'erro ao salvar o arquivo')

            else: # salva o arquivo caso o novo caminho seja diferente o antigo
                try: 
                    with open(arquivo + '.xml', 'w') as xml:
                            xml.write(self.dados)
                            self.varArquivo.clear()
                            self.lbArquivo.clear()
                            
                            QMessageBox.information(
                            self, 'salvo como sucesso', f'local do arquivo {arquivo}')
                            os.remove(self.urlArquivo)
                            
                except FileExistsError:
                    QMessageBox.critical(self, 'ops erro!!',
                                'esse arquivo não existe')
                except FileNotFoundError:
                    QMessageBox.critical(self, 'ops erro!!',
                                'erro ao salvar o arquivo')

    # função para limpar todo os campos do formularios
    def limpar(self):  
        self.varRamal.clear()
        self.varSenha.clear()

    # função para verificação do furmulario
    def verificarFormulario(self):
        # salva dos dados que é pego na tela para o sistema
        ramal = self.varRamal.text().strip()
        valorSenha = self.varSenha.text().strip()

        # verificação de todos os campos 
        if (not funcao.validarStr(ramal)):
            QMessageBox.critical(self, 'ops erro!!',
                                 'insira um valor para a ramal correto')
            return False
        elif (not funcao.validarStr(valorSenha)):
            QMessageBox.critical(
                self, 'ops erro!!', 'insira um valor para a senha do autor correto')
            return False

        return True

# inicia a tela
qt = QApplication(sys.argv)
ig = TratadoXml()
ig.show()
qt.exec_()
