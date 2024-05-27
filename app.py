"""""""""
CABEÇALHO:
---------------------
MÓDULO: app.py
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
DESCRIÇÃO: ESTE MÓDULO LIDA COM GERENCIAMENTO DE ROTAS E CADASTROS E VALIDAÇÃO DE USUÁRIOS EM UM BANCO SQLALCHEMY, JUNTO A ISSO CONSUMO DA GOOGLE PLACES API TANTO PARA O BACKEND QUANDO PARA O FRONT-END
CALCULANDO AS ROTAS A DISTÂNCIA E OBTENDO AS COORDENADAS PARA O FUNCIONAMENTO CORRETO DO APLICATIVO.
--------------------------------------------------------------------------------------
AUTOR DO CÓDIGO: GUSTAVO GANTOIS CARIA CARVALHO
-------------------------------------------------------------------------------------
DATA DA REALIZAÇÃO DO CÓDIGO DE ROTAS COM FLASK: 19/05/2024 
--------------------------------------------------------------------------------------
DATA DA REALIZAÇÃO DO CÓDIGO DO BANCO DE DADOS COM O SQLALCHEMY: 21/05/2024 
---------------------------------------------------------------------------------------

DEPENDÊNCIAS:

- FLASK
- SQLAlchemy
-bcrypt

FUNÇÕES:

-def login() = nesta função terá toda a lógica do backend da página de login com a validação dos dados, caso o usuário esteja cadastrado no banco ele conseguirá ter acesso ao App infinity 2.0, caso contrario ele não terá acesso.
-def site() = nestá função terá toda a renderização da página HTML do aplicativo.
-def cadastro() = nesta função terá toda a lógica do backend da página de cadastro com a captura de todos os dados recebidos através do formulário, com isso depois do cadastro ele terá acesso ao aplicativo infinity 2.0, caso ele não se cadastre, não será possivel ter o acesso.
-def delete() = nesta função terá toda a lógica do backend da página de delete com a captura dos dados através do formulário delete, depois que o usuário preencher os campos ele será removido do banco de dados, logo não terá mais acesso ao aplicativo.
-def deleteSucess() = nestá função terá a lógica para retornar a página html informando que a conta do usuário foi deletada com sucesso e junto a isso, uma mensagem no email, informando o mesmo.
-def send_email() = nestá função terá a lógica de enviar os dados de exclusão e cadastro do usuário para o email do mesmo.
-def obter_coordenadas() = nestá função terá a lógica de pegar os dados da API_KEY através do Google Places API e enviara os dados para o back-end (tanto para o backend quando para o front-end).
-def calcular_distancia() = nestá função terá a lógica para pegar o calculo da distãncia através da API obtendo as coordenadas, com isso dando as informações necessárias para criação do aplicativo Infinity 2.0.
-def index() = Irá renderizar o template index HTML para o HTML com o render_template.
-def calcular_rota() = nestá função terá a lógica para calcular as rotas de cada campo especificado nos inputs do formulário do app Infinity 2.0.
"""""""""


#Importando o JSON
import json
#improtando o os para enviar um email usando um servidor SMTP
import os
#Importando o smtplib para enviar email
import smtplib
#Importando o bcrypt para criptografar a senha.
import bcrypt
#Importando os requests para requerir insformações HTTP
import requests
#Importando o email.mine.text para mostrar que o usuário foi cadastrado no seu email.
from email.mime.text import MIMEText
#Importando o Flask
#render template para renderizar as informações na web

#Utilizando o redirect para redirecionar as rotas
#Utilizando a importação de Url
#Utilizando a importação do flash para mostrar mensagens
#Utilizando o jsonfy para importar o jsonfy para APIs
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
#Importando o SQL Alchemy no Flask
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define uma chave secreta para a sessão do Flask (necessária para utilizar flash messages)
GOOGLE_API_KEY = 'AIzaSyC_60gop36OSgTMCA13l7OK1dWd63xP2A8'

#Definindo uma chave secreta para o flask conseguir rodar
app.config['SECRET_KEY'] = 'palavra_secreta123'
#Utilizando o SQL Alchemy para registros do Banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Registros.db'
#Mostrando as Track_modifications como false 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Linka o objeto do SQLAlchemy com o aplicativo Flask
db = SQLAlchemy(app)

# Definição dos modelos de banco de dados
class Usuario(db.Model):
    #Criando a coluna do ID como um tipo INTEIRO de cada usuário com uma chave primária e um autoincremento:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      #Criando a coluna do username como um tipo STRING de cada usuário e o valor NULO como FALSO.
    username = db.Column(db.String(50), nullable=False)
      #Criando a coluna do name como um tipo STRING de cada usuário e o valor NULO como FALSO.
    name = db.Column(db.String(50), nullable=False)
      #Criando a coluna do email como um tipo STRING de cada usuário e o valor NULO como FALSO.
    email = db.Column(db.String(100), unique=True, nullable=False)
     #Criando a password da coluna do tipo STRING de cada password/usuário e o valor NULO como FALSO.
    password = db.Column(db.String(200), nullable=False)
    #Criando o phone da coluna do tipo STRING de cada telefone do usuário e o valor NULO como FALSO.
    phone = db.Column(db.String(20), nullable=False)
    #Criando o confirm_password do tipo STRING de cada confirm_password e o valor NULO como FALSO.
    confirm_password = db.Column(db.String(200), nullable=False)
    #Criando o gender do tipo STRING de cada gênero e o valor NULO como FALSO.
    gender = db.Column(db.String(10), nullable=False)
    #Criando o born_date do tipo STRING de cada data de nascimento e o valor NULO como FALSO.
    born_date = db.Column(db.String(20), nullable=False)
    #Criando o address do tipo STRING de cada endereço e o valor NULO como FALSO.
    address = db.Column(db.String(200), nullable=False)
# Cria as tabelas no banco de dados
with app.app_context():
    #Criando o data base para todas as informações/dados db.create_all
    db.create_all()

# Rota para a página de login
@app.route('/', methods=['GET', 'POST'])

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
#Criando a função login onde nela tera toda a lógica backend da página de login
def login():
    #Utilizando uma Estrutura condicional no python para fazer a verificação e pegar as informações do formulário/inputs de login através do método(method) POST 
    if request.method == 'POST':
        #Pegando o nome do usuário através do método request.form.get()
        username = request.form.get('username')
         #Pegando o password do usuário através do método request.form.get()
        password = request.form.get('password')

        # Consulta o banco de dados para encontrar o primeiro usuário cujo nome de usuário corresponde ao fornecido.
        user = Usuario.query.filter_by(username=username).first()
        #Se o usuário existe a senha fornecida (após a codificação 'utf-8') corresponde à senha armazenada (também codificada para 'utf-8'):
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            #Renderiza o template 'site.html' e passa o nome do usuário autenticado para o template
            return render_template('site.html', nameUser=user.name)
        else:
            #Exibe uma mensagem flash informando que o usuário ou a senha são inválidos
            flash('Usuário ou senha inválidos')
            #Redireciona para a página de login através desse comando.
            return redirect(url_for('login'))
    #Renderiza o template 'login.html' caso o método HTTP seja GET ou se a autenticação falhar
    return render_template('login.html')

#Criando a rota do app com o flask para a parte principal do APP de rotas.
@app.route('/site', methods=['GET', 'POST'])
#Criando uma função chamada site
def site():
    #Retornando o site.html para aparecer na web
    return render_template('site.html')

#Rota cadastro com o flask para renderizar o mesmo.
@app.route('/cadastro', methods=['GET', 'POST'])
#Criando a função de cadastro:
def cadastro():
    #Fazendo uma validação com if e else, se o método request for = POST ele vai pegar todos os dados abaixo 
    if request.method == 'POST':
        #Pegando o nome de usuário do formulário
        username = request.form.get('username')
        #Pegando o nome completo do usuário no formulário
        name = request.form.get('name')
        #Pegando o email do usuário no formulário
        email = request.form.get('email')
        #Pegando o número de telefone do usuário no formulário
        phone = request.form.get('phone')
        #Pegando a senha do usuário no formularío
        password = request.form.get('password')
        #Confirmando a senha que o usuário botou no input anterior no formulário
        confirm_password = request.form.get('confirm_password')
        #Pegando o gênero do usuário no formulário
        gender = request.form.get('gender')
        #Pegando o endereço do usuário no formulário
        address = request.form.get('address')
        #Pegando a data de nascimento do usuário no formulário
        born_date = request.form.get('born_date')

        #Criptografando a senha através de método hash para melhorar a segurança do usuário
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        #Cria uma nova instância do modelo Usuário com os dados fornecidos
        new_user = Usuario(
            #Atribui o nome de usuário ao campo username do modelo 
            username=username,
            #Atribui o nome completo do usuário ao campo name do modelo
            name=name,
            #Atribui o email do usuário no campo do modelo
            email=email,
            #Atribui a senha do usuário no campo modelo e depois criptografa a mesma através de hashed_password.decode('utf-8)
            password=hashed_password.decode('utf-8'),
            # Atribui o número de telefone ao campo phone do modelo
            phone=phone,
             # Atribui a confirmação da senha ao campo confirm_password do modelo
            confirm_password=confirm_password,
             # Atribui o gênero do usuário ao campo gender do modelo
            gender=gender,
             # Atribui a data de nascimento ao campo born_date do modelo
            born_date=born_date,
            # Atribui o endereço do usuário ao campo address do modelo
            address=address
        )

        # Adiciona o novo usuário à sessão do banco de dados.
        db.session.add(new_user)
        # Efetiva as mudanças na sessão do banco de dados, tornando a adição do usuário permanente.
        db.session.commit()

        #Mostrando a mensagem flash Usuário cadastrado com sucecsso 
        flash('Usuário cadastrado com sucesso!')
        #Redirecionando ele para a página de login
        return redirect(url_for('login'))
    #Retornando o template cadastro.html para rodar no HTML 
    return render_template('cadastro.html')

# Rota para exclusão de conta
@app.route('/delete', methods=['GET', 'POST'])
#Criando a função de deletar o usuário com o def
def delete():
    #Criando uma validação com if (Estrutura Condicional) e pegando o formulário com o método POST
    if request.method == 'POST':
        #Pegando o email no formulário de delete
        email = request.form['email']
        #Pegando o password do formulário de delete
        password = request.form['password']
        #Pegando o confirm_password do formulário de delete
        confirm_password = request.form['confirm_password']

        #Fazendo um if e else para validação (Estrutura Condicional) se a senha não for igual ao confirmar senha ele irá dar erro e mostrar uma mensagem no flash
        if password != confirm_password:
            flash("As senhas não coincidem", 'error')
            #Retornando a url delete para a página.
            return redirect(url_for('delete'))

        # Recupera o usuário do banco de dados com o email fornecido.
        user = Usuario.query.filter_by(email=email).first()
         #Verifica se o usuário foi encontrado e se a senha fornecida corresponde à senha armazenada no banco de dados, utilizando bcrypt para descriptografar a senha armazenada.
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            # Se o usuário existir e as senhas coincidirem, prosseguir com a exclusão.
             # Remove o usuário da sessão do banco de dados.
            db.session.delete(user)
            # Efetiva as mudanças na sessão do banco de dados, tornando a exclusão do usuário permanente.
            db.session.commit()
            # Adiciona uma mensagem flash para informar que o usuário foi excluído com sucesso
            flash('Usuário excluído com sucesso!', 'success')
            # Redireciona para a página de sucesso de exclusão.
            return redirect(url_for('deleteSuccess'))
        #Senão acontecer o bloco de código acima irá acontecer o bloco de código abaixo:
        else:
            # Caso o usuário não tenha sido encontrado ou a senha esteja incorreta, adiciona uma mensagem flash de erro.
            flash('Usuário ou senha inválidos', 'error')
            # Redireciona de volta para a página de exclusão para tentar novamente.
            return redirect(url_for('delete'))
    # Renderiza o template 'delete.html', que é a página de exclusão de usuário.
    return render_template('delete.html')

#Criando a rota flask para a página deleteSucess 
@app.route('/deleteSuccess')
#Criando a função (def) deleteSucess onde ficará toda a lógica do código de usuário deletado com sucesso:
def deleteSuccess():
    #Retornando o template HTML da página web para renderizar/rodar na aplicação flask
    return render_template('deleteSuccess.html')

# Função para enviar email                                                                       ESTÁ É A PARTE QUE PRECISAMOS CORRIGIR ONDE NÃO ESTÁ ENVIANDO O EMAIL COM A MENSAGEM!!
def send_email(to_email, subject, body):
    from_email = os.getenv('FLASK_EMAIL')
    from_password = os.getenv('FLASK_EMAIL_PASSWORD')
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Falha ao enviar email: {str(e)}")

#IMPLEMENTANDO A API DO GOOGLE MAPS 

GOOGLE_API_KEY = 'AIzaSyC_60gop36OSgTMCA13l7OK1dWd63xP2A8'

# Define uma função para obter as coordenadas (latitude e longitude) de um endereço utilizando a Geocoding API do Google Maps.
def obter_coordenadas(endereco, chave_api):
    # Constrói a URL para a requisição à Geocoding API com o endereço e a chave da API.
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={endereco}&key={chave_api}"
    # Realiza a requisição GET à URL e armazena a resposta.
    resposta = requests.get(url)
    # Converte a resposta para JSON.
    dados = resposta.json()
    
    # Verifica se a resposta da API está OK.
    if dados['status'] == 'OK':
        # Extrai os dados de latitude e longitude do primeiro resultado retornado.
        resultado = dados['results'][0]
        coordenadas = resultado['geometry']['location']
        # Retorna as coordenadas.
        return coordenadas['lat'], coordenadas['lng']
    else:
        # Levanta uma exceção em caso de erro na solicitação à API.
        raise Exception("Erro na solicitação à Geocoding API: " + dados['status'])

# Define uma função para calcular a distância e a duração entre duas coordenadas utilizando a Distance Matrix API do Google Maps.
def calcular_distancia(origem_coords, destino_coords, chave_api):
    # Converte as coordenadas de origem e destino em strings no formato "latitude,longitude".
    origem = f"{origem_coords[0]},{origem_coords[1]}"
    destino = f"{destino_coords[0]},{destino_coords[1]}"
    # Constrói a URL para a requisição à Distance Matrix API com as coordenadas de origem e destino e a chave da API.
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origem}&destinations={destino}&mode=driving&key={chave_api}"
    # Realiza a requisição GET à URL e armazena a resposta.
    resposta = requests.get(url)
    # Converte a resposta para JSON.
    dados = resposta.json()

    # Verifica se a resposta da API está OK.
    if dados['status'] == 'OK':
        # Extrai os dados de distância e duração do elemento retornado.
        elemento = dados['rows'][0]['elements'][0]
        distancia = elemento['distance']['text']
        duracao = elemento['duration']['text']
        # Retorna a distância e a duração.
        return distancia, duracao
    else:
        # Levanta uma exceção em caso de erro na solicitação à API.
        raise Exception("Erro na solicitação à Distance Matrix API: " + dados['status'])

# Define a rota para a página inicial.
@app.route('/')
def index():
    # Renderiza o template 'index.html'.
    return render_template('index.html')

# Define a rota para a aplicação, onde são enviados os dados do formulário via POST.
@app.route('/app', methods=['POST'])
def calcular_rota():
    # Obtém os valores de origem e destino do formulário.
    origem = request.form.get('origem')
    destino = request.form.get('destino')
    
    try:
        # Obtém as coordenadas de origem e destino.
        origem_coords = obter_coordenadas(origem, GOOGLE_API_KEY)
        destino_coords = obter_coordenadas(destino, GOOGLE_API_KEY)
        
        # Calcula a distância e a duração da rota.
        distancia, duracao = calcular_distancia(origem_coords, destino_coords, GOOGLE_API_KEY)
        
        # Retorna os dados de distância e duração em formato JSON.
        return jsonify({'distancia': distancia, 'duracao': duracao})
    
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro em formato JSON.
        return jsonify({'error': str(e)}), 500
    
# Executa a aplicação Flask em modo de depuração.
if __name__ == '__main__':
    app.run(debug=True)


