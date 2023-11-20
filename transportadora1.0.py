import mysql.connector
from tkinter import *
from tkinter import simpledialog

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='transportadora',
)

cursor = conexao.cursor()


def cadastrar(): #Função para cadastrar 
    texto1.grid_forget() #Apagando informações da tela para adicionar novas
    create.grid_forget()
    read.grid_forget()
    update.grid_forget()
    delete.grid_forget()

    textoCadasCamin = Label(janela, text='Cadastrar Caminhão') #criando todos os textos e botões que serão usados
    txtmarca = Label(janela, text='Marca')
    marcaform = Entry(janela)
    txtkm = Label(janela, text='Quilometragem')
    kmform = Entry(janela)
    txtpreco = Label(janela, text='Preço')
    precoform = Entry(janela)
    txtdatarevisao = Label(janela, text='Data da revisão')
    datarevisaoform = Entry(janela)
    txtidmotorista = Label(janela, text='Id do motorista')
    idmotoristaform = Entry(janela)

    textoCadasCarg = Label(janela, text='Cadastrar Carga')
    txttipo = Label(janela, text='Tipo')
    tipoform = Entry(janela)
    txtpreco = Label(janela, text='Preço')
    precoform = Entry(janela)
    txtdistancia = Label(janela, text='Distância')
    distanciaform = Entry(janela)
    txtquantidade = Label(janela, text='Quantidade')
    quantidadeform = Entry(janela)
    txtdestinatario = Label(janela, text='Destinatário')
    destinatarioform = Entry(janela)
    txtmotoristaid = Label(janela, text='Id do motorista')
    motoristaidform = Entry(janela)

    textoCadasMotor = Label(janela, text='Cadastrar Motorista')
    txtnome = Label(janela, text='Nome')
    nomeform = Entry(janela)
    txtidade = Label(janela, text='Idade')
    idadeform = Entry(janela)
    txtcpf = Label(janela, text='CPF')
    cpfform = Entry(janela)
    txttelefone = Label(janela, text='Telefone')
    telefoneform = Entry(janela)
    txtsalario = Label(janela, text='Salário')
    salarioform = Entry(janela)
    txtcargahoraria = Label(janela, text='Carga horária')
    cargahorariaform = Entry(janela)

    def caminhoes(): #cadastro de caminhões
        texto2.grid_forget()
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        textoCadasCamin.grid(column=1, row=0, pady=20) #chamando os botões para a interface

        txtmarca.grid(column=0, row=1, padx=5, pady=10)
        marcaform.grid(column=1, row=1)
        

        txtkm.grid(column=0, row=2, padx=5, pady=10)
        kmform.grid(column=1, row=2)

        txtpreco.grid(column=0, row=3, padx=5, pady=10)
        precoform.grid(column=1, row=3)
        

        txtdatarevisao.grid(column=0, row=4, padx=5, pady=10)
        datarevisaoform.grid(column=1, row=4)

        txtidmotorista.grid(column=0, row=5, padx=30, pady=10)
        idmotoristaform.grid(column=1, row=5)
        

        enviarcaminhoes.grid(column=0, row=6, padx=10) #enviando informações

    def cargas(): 
        texto2.grid_forget()
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        textoCadasCarg.grid(column=1, row=0, pady=20) 

        txttipo.grid(column=0, row=1, padx=5, pady=10)
        tipoform.grid(column=1, row=1)
        

        txtpreco.grid(column=0, row=2, padx=5, pady=10)
        precoform.grid(column=1, row=2)
        

        txtdistancia.grid(column=0, row=3, padx=5, pady=10)
        distanciaform.grid(column=1, row=3)
        

        txtquantidade.grid(column=0, row=4, padx=5, pady=10)
        quantidadeform.grid(column=1, row=4)
        

        txtdestinatario.grid(column=0, row=5, padx=5, pady=10)
        destinatarioform.grid(column=1, row=5)

        txtmotoristaid.grid(column=0, row=6, padx=30, pady=10)
        motoristaidform.grid(column=1, row=6)
        

        enviarcargas.grid(column=0, row=7, padx=10) 


    def motoristas(): 
        texto2.grid_forget()
        caminhao.destroy()
        carga.grid_forget()
        motorista.grid_forget()

        textoCadasMotor.grid(column=1, row=0, pady=20)

        txtnome.grid(column=0, row=1, padx=5, pady=10)
        nomeform.grid(column=1, row=1)
        

        txtidade.grid(column=0, row=2, padx=5, pady=10)
        idadeform.grid(column=1, row=2)
    

        txtcpf.grid(column=0, row=3, padx=5, pady=10)
        cpfform.grid(column=1, row=3)
        

        txttelefone.grid(column=0, row=4, padx=5, pady=10)
        telefoneform.grid(column=1, row=4)
        

        txtsalario.grid(column=0, row=5, padx=5, pady=10)
        salarioform.grid(column=1, row=5)
        

        txtcargahoraria.grid(column=0, row=6, padx=5, pady=10)
        cargahorariaform.grid(column=1, row=6)
        

       
        enviarmotoristas.grid(column=0, row=7, padx=10) 


    def submitcaminhao(marca, km, preco, datarevisao, idmotorista): #função para enviar com os parâmetros
        enviarcaminhoes.grid_forget()
        txtmarca.grid_forget()
        txtkm.grid_forget()
        txtpreco.grid_forget()
        txtdatarevisao.grid_forget()
        marcaform.grid_forget()
        kmform.grid_forget()
        precoform.grid_forget()
        datarevisaoform.grid_forget()
        txtidmotorista.grid_forget()
        idmotoristaform.grid_forget()
        textoCadasCamin.grid_forget()
        

        comando = f'INSERT INTO caminhoes (marca, km, preco, datarevisao, idmotorista) VALUES ("{marca}", {km}, {preco}, "{datarevisao}", {idmotorista})'
        cursor.execute(comando) #comando SQL
        conexao.commit()

        texto1.grid(column=1, row=0, pady=20)
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10) #chamando o menu novamente


    def submitcarga(tipo, preco, distancia, quantidade, destinatario, motoristaid): #função para enviar com os parâmetros
        enviarcargas.grid_forget()
        textoCadasCarg.grid_forget()
        txttipo.grid_forget()
        tipoform.grid_forget()  
        txtpreco.grid_forget()  
        precoform.grid_forget() 
        txtdistancia.grid_forget()  
        distanciaform.grid_forget()  
        txtquantidade.grid_forget() 
        quantidadeform.grid_forget() 
        txtdestinatario.grid_forget()  
        destinatarioform.grid_forget()
        txtmotoristaid.grid_forget()
        motoristaidform.grid_forget()  
        
        comando = 'INSERT INTO cargas (tipo, preco, distancia, quantidade, destinatario, motoristaid) VALUES (%s, %s, %s, %s, %s, %s)'
        valores = (tipo, preco, distancia, quantidade, destinatario, motoristaid)
        cursor.execute(comando, valores) #comandos SQL
        conexao.commit()

        texto1.grid(column=1, row=0, pady=20) #chamando menu
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10)

    def submitmotorista(nome, idade, cpf, telefone, salario, cargahoraria): 
        enviarmotoristas.grid_forget()
        textoCadasMotor.grid_forget()
        txtnome.grid_forget()
        nomeform.grid_forget()  
        txtidade.grid_forget()  
        idadeform.grid_forget() 
        txtcpf.grid_forget()  
        cpfform.grid_forget()  
        txttelefone.grid_forget() 
        telefoneform.grid_forget() 
        txtsalario.grid_forget()  
        salarioform.grid_forget()  
        txtcargahoraria.grid_forget()  
        cargahorariaform.grid_forget()  


        comando = f'INSERT INTO motoristas (nome, idade, cpf, telefone, salario, cargahoraria) VALUES ("{nome}", {idade}, {cpf}, {telefone}, {salario}, {cargahoraria})'
        cursor.execute(comando) 
        conexao.commit()

        texto1.grid(column=1, row=0, pady=20)
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10)

    #Criando botões e passando parâmetros
    enviarmotoristas = Button(janela, text='Enviar', command=lambda: [submitmotorista(nomeform.get(), idadeform.get(), cpfform.get(), telefoneform.get(), salarioform.get(), cargahorariaform.get())])
    enviarcargas = Button(janela, text='Enviar', command=lambda: [submitcarga(tipoform.get(), precoform.get(), distanciaform.get(), quantidadeform.get(), destinatarioform.get(), motoristaidform.get())])
    enviarcaminhoes = Button(janela, text='Enviar', command=lambda: [submitcaminhao(marcaform.get(), kmform.get(), precoform.get(), datarevisaoform.get(), idmotoristaform.get())])
    
    #Menu do create
    texto2 = Label(janela, text='Escolha qual o tipo de cadastro')
    texto2.grid(column=1, row=0, pady=20)

    caminhao = Button(janela, text='Cadastrar caminhão', command=caminhoes)
    caminhao.grid(column=0, row=1, padx=30, pady=10)

    carga = Button(janela, text='Cadastrar carga', command=cargas)
    carga.grid(column=1, row=1, padx=30, pady=10)

    motorista = Button(janela, text='Cadastrar motorista', command=motoristas)
    motorista.grid(column=2, row=1, padx=30, pady=10)

    
def visualizar(): #def para visualizar
    texto1.grid_forget()
    create.grid_forget()
    read.grid_forget()
    update.grid_forget()
    delete.grid_forget()


    def caminhoes(): #visualizar caminhões
        linha = 1
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        comando = f'SELECT * FROM caminhoes' #comando SQL
        cursor.execute(comando)
        resultado = cursor.fetchall()
        lista = []
        for i in resultado: #mostrando informações
            valores = Label(janela, text='ID\tMarca\tQuilometragem\tPreço\t\tRevisão\t\tID motorista'
                            f'\n{i[0]}\t{i[1]}\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t{i[5]}\n')
            lista.append(valores) #inserindo valores para poder tirar da tela depois
            valores.grid(column=0, row=linha)
            linha += 1
        
        linha += 1
        voltar = Button(janela, text='Voltar', command=lambda: menu()) #botao para voltar
        voltar.grid(column=4, row=linha, padx=30, pady=10)

        def menu(): #voltando ao menu
            for valores in lista:
                valores.grid_forget() #apagando informações
            lista.clear()
            voltar.grid_forget()
            texto1.grid(column=1, row=0, pady=20)
            create.grid(column=0, row=1, padx=30, pady=10)
            read.grid(column=1, row=1, padx=30, pady=10)
            update.grid(column=2, row=1, padx=30, pady=10)
            delete.grid(column=3, row=1, padx=30, pady=10)

    def cargas():
        linha = 1
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        comando = f'SELECT * FROM cargas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        lista = []


        for i in resultado:
            valores = Label(janela, text='ID\tTipo\tPreço\tDistância\tQuantidade\tDestinatário\t\tID motorista'
                            f'\n{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t\t{i[4]}\t{i[5]}\t{i[6]}')
            lista.append(valores)
            valores.grid(column=0, row=linha)
            linha += 1
        
        linha += 1
        voltar = Button(janela, text='Voltar', command=lambda: [menu()])
        voltar.grid(column=4, row=linha, padx=30, pady=10)
        
        def menu():
            for valores in lista:
                valores.grid_forget()
            lista.clear()
            voltar.grid_forget()
            texto1.grid(column=1, row=0, pady=20)
            create.grid(column=0, row=1, padx=30, pady=10)
            read.grid(column=1, row=1, padx=30, pady=10)
            update.grid(column=2, row=1, padx=30, pady=10)
            delete.grid(column=3, row=1, padx=30, pady=10)
    
    def motoristas():
        linha = 1
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        comando = f'SELECT * FROM motoristas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        lista = []
        for i in resultado:
            valores = Label(janela, text='ID\tNome\tIdade\tCPF\tTelefone\tSalário\tCargaHorária'
                            f'\n{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}')
            lista.append(valores)
            valores.grid(column=0, row=linha)
            linha += 1
        
        linha += 1
        voltar = Button(janela, text='Voltar', command=lambda: [menu()])
        voltar.grid(column=4, row=linha, padx=30, pady=10)

        def menu():
            for valores in lista:
                valores.grid_forget()
            lista.clear()
            voltar.grid_forget()
            texto1.grid(column=1, row=0, pady=20)
            create.grid(column=0, row=1, padx=30, pady=10)
            read.grid(column=1, row=1, padx=30, pady=10)
            update.grid(column=2, row=1, padx=30, pady=10)
            delete.grid(column=3, row=1, padx=30, pady=10)

    #menu do visualizar
    caminhao = Button(janela, text='Visualizar Caminhões', command=caminhoes)
    caminhao.grid(column=0, row=1, padx=30, pady=10)

    carga = Button(janela, text='Visualizar Cargas', command=cargas)
    carga.grid(column=1, row=1, padx=30, pady=10)

    motorista = Button(janela, text='Visualizar Motoristas', command=motoristas)
    motorista.grid(column=2, row=1, padx=30, pady=10)



def editar_campo(tipo, id_registro): #função de editar
    def submit_edicao(coluna, novo_valor):
        comando = f'UPDATE {tipo} SET {coluna} = "{novo_valor}" WHERE id = {id_registro}' #comando SQL
        cursor.execute(comando)
        conexao.commit()
        janela_edicao.destroy()

    colunas_caminhao = ["marca", "km", "preco", "datarevisao", "idmotorista"] #Colunas para selecionar o que vai ser editado
    colunas_carga = ["tipo", "preco", "distancia", "quantidade", "destinatario", "motoristaid"]
    colunas_motorista = ["nome", "idade", "cpf", "telefone", "salario", "cargahoraria"]

    if tipo == "caminhoes": 
        colunas = colunas_caminhao
    elif tipo == "cargas":
        colunas = colunas_carga
    elif tipo == "motoristas":
        colunas = colunas_motorista
    else:
        return

    janela_edicao = Tk()
    janela_edicao.title(f'Editar {tipo.capitalize()} - ID {id_registro}')

    label_coluna = Label(janela_edicao, text='Escolha o campo a ser editado:')
    label_coluna.grid(column=0, row=0, padx=10, pady=10)

    coluna_var = StringVar()
    coluna_var.set(colunas[0]) 
    dropdown_coluna = OptionMenu(janela_edicao, coluna_var, *colunas)
    dropdown_coluna.grid(column=1, row=0, padx=10, pady=10)

    label_novo_valor = Label(janela_edicao, text='Novo valor:')
    label_novo_valor.grid(column=0, row=1, padx=10, pady=10)

    novo_valor_entry = Entry(janela_edicao)
    novo_valor_entry.grid(column=1, row=1, padx=10, pady=10)

    def submit():
        coluna_selecionada = coluna_var.get()
        novo_valor = novo_valor_entry.get()
        if novo_valor:
            submit_edicao(coluna_selecionada, novo_valor)
        else:
            print('Preencha o novo valor.')

    botao_submit = Button(janela_edicao, text='Salvar', command=submit)
    botao_submit.grid(column=0, row=2, columnspan=2, pady=10)
def editar():
    tipo_cadastro = simpledialog.askstring("Editar", "Escolha o tipo de cadastro (caminhoes, cargas, motoristas):")
    if tipo_cadastro:
        id_registro = simpledialog.askinteger("Editar", "Digite o ID do registro que deseja editar:")
        if id_registro:
            editar_campo(tipo_cadastro, id_registro)
        
        


def deletar(): #função de deletar
    texto1.grid_forget()
    create.grid_forget()
    read.grid_forget()
    update.grid_forget()
    delete.grid_forget()

    idcaminhao = Entry(janela) #botões e textos
    txt = Label(janela, text='ID que deseja deletar')

    idcarga = Entry(janela)

    idmotorista = Entry(janela)

    submitcaminhao = Button(janela, text='Enviar', command=lambda: [caminhaosubmit(idcaminhao.get())])

    submitcarga = Button(janela, text='Enviar', command=lambda: [cargasubmit(idcarga.get())])

    submitmotorista = Button(janela, text='Enviar', command=lambda: [motoristasubmit(idmotorista.get())])

    def caminhoes(): #função específica para deletar
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        txt.grid(column=0, row=1, padx=30, pady=10) #Inputs
        idcaminhao.grid(column=1, row=1, padx=30, pady=10)

        submitcaminhao.grid(column=0, row=2, padx=30, pady=10) #botão de enviar

    def cargas():
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        txt.grid(column=0, row=1, padx=30, pady=10)
        idcarga.grid(column=1, row=1, padx=30, pady=10)

        submitcarga.grid(column=0, row=2, padx=30, pady=10)

    def motoristas():
        caminhao.grid_forget()
        carga.grid_forget()
        motorista.grid_forget()

        txt.grid(column=0, row=1, padx=30, pady=10)
        idmotorista.grid(column=1, row=1, padx=30, pady=10)

        submitmotorista.grid(column=0, row=2, padx=30, pady=10)


    def caminhaosubmit(id): #enviando com o parâmetro ID
        
        comando = f'DELETE FROM caminhoes WHERE id = {id}' #comando SQL
        cursor.execute(comando)
        conexao.commit()
        txt.grid_forget()
        idcaminhao.grid_forget()
        submitcaminhao.grid_forget()

        texto1.grid(column=1, row=0, pady=20) #voltando ao menu
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10)
    

    def cargasubmit(id):
        id = (idcarga.get())
        comando = f'DELETE FROM cargas WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        txt.grid_forget()
        idcarga.grid_forget()
        submitcarga.grid_forget()

        texto1.grid(column=1, row=0, pady=20)
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10)

    def motoristasubmit(id):
        id = (idmotorista.get())
        comando = f'DELETE FROM motoristas WHERE id = {id}'
        cursor.execute(comando)
        conexao.commit()
        txt.grid_forget()
        idmotorista.grid_forget()
        submitmotorista.grid_forget()

        texto1.grid(column=1, row=0, pady=20)
        create.grid(column=0, row=1, padx=30, pady=10)
        read.grid(column=1, row=1, padx=30, pady=10)
        update.grid(column=2, row=1, padx=30, pady=10)
        delete.grid(column=3, row=1, padx=30, pady=10)

    #menu delete
    caminhao = Button(janela, text='Deletar Caminhão', command=caminhoes)
    caminhao.grid(column=0, row=1, padx=30, pady=10)

    carga = Button(janela, text='Deletar Carga', command=cargas)
    carga.grid(column=1, row=1, padx=30, pady=10)

    motorista = Button(janela, text='Deletar Motorista', command=motoristas)
    motorista.grid(column=2, row=1, padx=30, pady=10)



       
#menu principal
janela = Tk()
janela.title('Transportadora')

texto1 = Label(janela, text='Escolha o que deseja fazer')
texto1.grid(column=1, row=0, pady=20)

create = Button(janela, text='Cadastrar', command=cadastrar)
create.grid(column=0, row=1, padx=30, pady=10)

read = Button(janela, text='Visualizar cadastros', command=visualizar)
read.grid(column=1, row=1, padx=30, pady=10)

update = Button(janela, text='Atualizar cadastro', command=editar)
update.grid(column=2, row=1, padx=30, pady=10)

delete = Button(janela, text='Deletar cadastro', command=deletar)
delete.grid(column=3, row=1, padx=30, pady=10)

janela.mainloop()