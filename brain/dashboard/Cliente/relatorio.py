#!/usr/bin/sh
import os
from pathlib import Path

from PyQt5.QtWidgets import QFileDialog, QAction
from pylatex import Document, Head, Subsection, Tabular, MultiColumn, \
    Command, NoEscape, Tabularx, MiniPage, StandAloneGraphic, Tabu, PageStyle, Foot, simple_page_number, LongTabu, \
    FlushLeft
from pylatex.utils import bold
from pylatex.basic import NewLine, LargeText, LineBreak, MediumText, TextColor, NewPage

import datetime
import pandas as pd

from brain.DAOs.UserConfig import DaoConfiguracoes
from brain.DAOs.daoCliente import DaoCliente
from brain.funcoesAuxiliares import mascaraMeses
from modelos.usuarioModel import UsuarioModel
from brain.funcoesAuxiliares import mascaraCNPJ


class RelatorioCliente:

    def __init__(self, nomeArquivo, usuario, db=None):
        self.nomeArquivo = nomeArquivo
        self.usuarioModel = UsuarioModel().fromList(usuario)

        self.geometry = {'head': '40pt', 'margin': '1.5cm', 'tmargin': '1cm', 'includeheadfoot': True}
        self.documento = Document(f'{self.nomeArquivo}', geometry_options=self.geometry, page_numbers=False)
        self.firstPage = None

        self.daoClientes = DaoCliente(db=db)

        # Estatísticas
        self.totalClientes = 0
        self.clientesAtivos = 0
        self.clientesInativos = 0
        self.mediaClientesAtivos = 0
        self.clientesList = None
        self.carregarClientes()
        self.contaTotalClientes()

    def constroiCabecalho(self):
        self.firstPage = PageStyle('firstpage')

        with self.firstPage.create(Head("L")) as header_left:
            with header_left.create(MiniPage(width=NoEscape(r"0.3\textwidth"), pos='l')) as logo_wrapper:
                with logo_wrapper.create(Tabularx('X X', width_argument=NoEscape(r"0.5\textwidth"))) as logo:
                    logo.add_row([MultiColumn(2, align='c')])
                    logo_file = os.path.join(os.getcwd(), 'Telas', 'Imagens', 'nautilusDash.png')
                    imagem = StandAloneGraphic(image_options="width=36px", filename=logo_file)
                    textLogo = MiniPage(width=NoEscape(r"0.6\textwidth"), content_pos='t', align='l')

                    textLogo.append(LargeText(bold('Nautilus')))
                    textLogo.append(LineBreak())
                    textLogo.append('Navegue sem medo')
                    textLogo.append(LineBreak())
                    textLogo.append('\n')

                    logo.add_row([imagem, textLogo])

        with self.firstPage.create(Head("C")) as headerCenter:
            with headerCenter.create(MiniPage(width=NoEscape(r"0.4\textwidth"), pos='c')) as centro:
                centro.append(LargeText(bold('Relatório geral de clientes')))

        # Add document title
        with self.firstPage.create(Head("R")) as right_header:
            with right_header.create(MiniPage(width=NoEscape(r"0.3\textwidth"), pos='R', align='r')) as title_wrapper:
                title_wrapper.append(LargeText(bold(self.usuarioModel.nomeEmpresa)))
                title_wrapper.append(LineBreak())
                title_wrapper.append(MediumText(mascaraMeses(data=datetime.date.today())))

    def constroiCorpo(self):

        with self.documento.create(Tabu("X[l] X[r]")) as first_page_table:
            customer = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='h')
            customer.append(bold("Nome fantasia: "))
            customer.append(self.usuarioModel.nomeFantasia)
            customer.append("\n")
            customer.append(bold("CNPJ: "))
            customer.append(mascaraCNPJ(self.usuarioModel.cnpj))
            customer.append("\n")
            customer.append(bold("Endereço: "))
            if self.usuarioModel.endereco == 'None':
                customer.append('---')
            else:
                customer.append(self.usuarioModel.endereco)

            # Add branch information
            branch = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!', align='r')
            branch.append(f"Total de clientes: {self.totalClientes}")
            branch.append(LineBreak())
            branch.append(f"Total de clientes Ativos: {self.clientesAtivos}")
            branch.append(LineBreak())
            branch.append(f"Média de clientes ativos: {round((self.clientesAtivos / self.totalClientes)*100)} % ")
            branch.append(LineBreak())

            first_page_table.add_row([customer, branch])
            first_page_table.add_empty_row()

        self.documento.change_document_style("firstpage")

        with self.documento.create(LongTabu("X[1.5l] X[2l] X[r] X[r] X[r]", row_height=1.5)) as data_table:
            data_table.add_row(["Última atualização",
                                "Nome do cliente",
                                "Turma",
                                "credits($)",
                                "balance($)"],
                               mapper=bold,
                               color="lightgray")
            data_table.add_empty_row()
            data_table.add_hline()
            for i, cliente in enumerate(self.clientesList):
                clienteRow = list()
                clienteRow.append(mascaraMeses(cliente[13]))
                clienteRow.append(cliente[1]+' '+cliente[2])
                clienteRow.append('Teste 1')
                clienteRow.append('Teste 2')
                clienteRow.append('Teste 3')
                if (i % 2) == 0:
                    data_table.add_row(clienteRow, color="lightgray")
                else:
                    data_table.add_row(clienteRow)

    def exportaRelatorio(self, tipo='pdf'):

        # Desenvolvimento
        fileName = QFileDialog.getSaveFileName(directory=str(Path.home()), options=QFileDialog.DontUseNativeDialog, filter="Adobe Pdf (*.pdf);;Excel (*.xlsx)")

        # Produção
        # fileName = QFileDialog.getSaveFileName(directory=str(Path.home()), filter="Adobe Pdf (*.pdf);;Excel (*.xlsx)")
        print(f'\033[33m{fileName}')

        if fileName[0] != '':
            if '*.pdf' in fileName[1]:
                self.constroiCabecalho()
                self.constroiCorpo()
                self.documento.preamble.append(self.firstPage)
                self.documento.generate_pdf(fileName[0], clean_tex=False)
            else:
                self.exportaExcel(fileName[0])

    def contaTotalClientes(self):
        self.totalClientes = self.daoClientes.contaTotal()
        self.clientesAtivos = self.daoClientes.contaTotal(where='WHERE ativo = TRUE')
        self.clientesInativos = self.totalClientes - self.clientesAtivos

    def carregarClientes(self):
        self.clientesList = self.daoClientes.findAll(all=True)

    def exportaExcel(self, path):

        colunas = ['Inscrição', 'Nome', 'Sobrenome', 'Telefone', 'E-mail', 'CPF',
                   'Endereço', 'Complemento', 'CEP', 'Bairro', 'Meio de Pagamento',
                   'Usuário ativo', 'Data do Cadastro', 'Última atualização']

        dataFrameClientes = pd.DataFrame(self.clientesList, columns=colunas)

        excelWriter = pd.ExcelWriter(f'{path}.xlsx', endine='openpyxl')

        dataFrameClientes.to_excel(excel_writer=excelWriter, index=False)
        excelWriter.save()


if __name__ == '__main__':
    config = DaoConfiguracoes()
    relatorio = RelatorioCliente(nomeArquivo='Relatório de clientes', usuario=config.buscaUsuarioAtivo())
    # relatorio.exportaRelatorio()
    relatorio.exportaRelatorio(tipo='excel')