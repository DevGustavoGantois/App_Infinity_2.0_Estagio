INFELIZMENTE NÃO CONSEGUI FAZER O DEPLOY DA APLICAÇÃO.

<h1>Infinity App 2.0 com Flask</h1>
<h2>Desafio realizado para conseguir a vaga na empresa</h2>
-------------------------------------------------------------------------------------------------------------------
<h3>
  Requisitos do projeto feito:
</h3>

Regras do Infinity 2.0 App

1. Comentários no Código
   
● Todas as linhas de código devem ser comentadas.

2. Documentação do Código
   
● Todo código deve conter documentação no cabeçalho.

3. Nomenclatura das Colunas no Banco de Dados
   
● Utilize apenas letras minúsculas e sem caracteres especiais nos nomes das
colunas.

● Espaços não são permitidos, use apenas _ (underscore) para separar
palavras.

4. Criação de Colunas
   
● Nunca crie uma coluna com valor NONE ou NULL.

5. Armazenamento de Informações em Colunas
   
● Sempre que passar mais de uma informação para uma coluna, deve ser
usada uma lista.

● Se dentro dessa lista houver mais características, use um dicionário.

6. Limite de Requisições em Páginas

● Em uma página carregada, não pode haver mais de três requisições ao
banco de dados para buscar dados.

7. Agrupamento de Requisições Update
   
● Todas as requisições de atualização (update) ao banco de dados devem
estar agrupadas em uma única requisição.

8. Conexões com o Banco de Dados
  
● Ao fazer uma conexão, é necessário abrir e fechar a requisição.

9. Limite de Cascata de Requisições
    
● Não é permitido fazer cascata de requisições no banco SQL, sendo permitido
no máximo dois bancos interconectados para uma única requisição.

10. Identificador Universal
    
● Utilize um identificador universal para comunicação entre os bancos de
dados.

12. Variável de Retorno em Funções
● Todas as funções devem ter uma variável chamada retorno.

13. JSON de Retorno em Páginas
    
● Todas as páginas devem ter um JSON chamado retorno.

14. Comunicação entre Páginas no Flask
    
● Apenas uma variável pode ser usada para as comunicações entre as páginas
no Flask, e deve ser um JSON.

15. Tratamento de Campos de Input
    
● Todo campo de input em uma página deve ter tratamento de string para
evitar erros de caracteres especiais e caixa alta.

16. Atualização de Dados em Páginas
    
● Páginas que mostram dados devem usar AJAX com atualizações em
intervalos curtos para novos dados.

17. Uso de Javascript e Python
    
● Use Javascript apenas quando não for possível usar Python.

18. Uso de APIs
    
● Não é permitido usar SDK para APIs, apenas requisições manuais.

19. Colunas sem Uso
    
● Não pode haver colunas sem uso no banco de dados.

20. Nomes de Variáveis
    
● Não pode haver duas variáveis com o mesmo nome, mesmo que em códigos
ou funções diferentes.

Testes de Regras
Descrição do Projeto

Crie um servidor Flask para mediar a distância entre o endereço cadastrado e o endereço
da mercadoria cadastrada apos acesso ao login e faça uma previsão de tempo de entrega
usando um automóvel. O servidor deve incluir:

1. Página de Login
● Acesso do usuário ao sistema.

2. Página de Cadastro e Exclusão de Usuário
   
● Funcionalidades de registro e remoção de usuários.
● Deve haver confirmação por email para concluir o cadastro.

3. Informações do Endereço via API
   
● Ao fazer o login, o usuário acessará informações do endereço usando uma
API, fornecendo coordenadas, CEP e outras informações.

5. Arquitetura de Bancos de Dados
   
● Criação de bancos para registros dos dados e dos logs dos usuários.

6. Páginas com AJAX
   
● Páginas de demonstração devem usar AJAX para atualizar o tempo de
entrega com base no tempo atual.

Implementação do Projeto

6. Configuração do Servidor Flask
   
● Configurar o ambiente Flask com as rotas para login, cadastro e exclusão de
usuários.
● Implementar verificação de email para confirmação de cadastro.

8. Integração com API de Geolocalização
   
● Usar uma API para obter informações de localização e calcular a distância
entre endereços.

10. Estrutura de Bancos de Dados
    
● Criar tabelas com nomes de colunas em letras minúsculas e sem caracteres
especiais.
● Armazenar registros de usuários e logs das atividades.

12. Páginas Dinâmicas com AJAX
   
● Implementar páginas que atualizam o tempo de entrega em intervalos curtos
usando AJAX.
● Garantir que a comunicação entre páginas seja feita através de JSON.

10. Regras de Codificação
    
● Seguir todas as regras de codificação e boas práticas mencionadas nas
regras do Infinity 2.0 App.


------------------------------------------------------------------------

![Captura de tela 2024-05-23 222730](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/50d59edf-50f3-4c3a-ac51-d12a2d331d86)


-------------------------------------------------------------------------


![Captura de tela 2024-05-23 223631](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/0de4174f-093b-451a-a271-7e48718027fd)


-------------------------------------------------------------------------


![Captura de tela 2024-05-23 223325](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/f168dfe8-39a4-4d47-a26e-50b21839444f)


-------------------------------------------------------------------------


![Captura de tela 2024-05-23 223403](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/ca8e2578-c6d9-45e3-9ad8-eaea0d0f575e)


--------------------------------------------------------------------------

![Captura de tela 2024-05-19 174441](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/f3979691-dbe5-4ddf-9b5d-8d902ecded8f)


---------------------------------------------------------------------------

![Captura de tela 2024-05-19 170827](https://github.com/DevGustavoGantois/App_Infinity_2.0_Estagio_Desafio/assets/123424700/872552bc-0625-4a08-b6f1-51b43bf894bd)
