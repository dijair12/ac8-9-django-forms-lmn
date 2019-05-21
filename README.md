# Exercício Django Formulários

# Enunciado
Nessa atividade serão criados os formulários no Django, para validação de dados e algumas regras de negócio. Deverá ser utilizada a API de Form do Django.

Também será feito um cadastro completo, do HTML até o banco de dados. Além do ORM do Django, deve ser utilizado o formulário para cadastro.

## Como começar
Após a clonagem, vocês devem fazer os formulários e testá-los. Os formulários feitos em HTML são modelos para você se basear e saber um pouco mais dos dados, o mais importante são as regras de validação dos formulários Django.

Todos as classes de formulários já estão prontas, vocês devem apenas completar os formulários, estendendo a classe correta do Django, listando os campos e as regras de negócio.

## Instruções Técnicas

As classes dos formulários estão criadas nas suas respectivas aplicações. Vocês devem apenas preencher os campos e os métodos necessários. Todos possuem um método adicional, esse método não deve ter seu nome alterado, apenas preenchido com o códgio Python para a sua correta execução.

### Formulários

Devem ser criados os formulários citados abaixo, cada um com sua respectiva página e _view_. Os formulários devem validar conforme as regras apresentadas.

Cada formulário possui um método adicional, que deve executar a regra de negócio especificada nele. Esse método deve ser disparado se o formulário estiver válido.

#### Contato

Esse formulário deve estar associado à página de contato na aplicação **website**. Ele deve coletar os campos iguais ao formulário HTML e fazer as seguintes validações:
 
 - O campo _nome_ é obrigatório e deve ter no máximo 120 caracteres.
 - O campo _email_ só é obrigatório se o tipo de resposta incluir e-mail (erro: "E-mail é obrigatório quando for escolhido como resposta."). Caso o e-mail esteja preenchido, ele deve ser válido.
 - O campo _telefone_ só é obrigatório se o tipo de resposta incluir telefone (erro: "Telefone é obrigatório quando for escolhido como resposta.").
 - O campo _assunto_ é obrigatório e deve verificar se o escolhido foi uma das três opções válidas (B,R ou S).
 - O campo _mensagem_ é obrigatório.
 - O campo _resposta_ não é obrigatório, mas quando preenchido deve conter apenas as opções válidas (T ou E).

 Além disso, o método **enviar_email** do formulário deve enviar um e-mail com os dados passados no formulário, da mesma maneira que está atualmente na _view_ contato.

#### Entrar
O formulário deve estar associado à página de login na aplicação **contas**. Além disso deve validar:
 
 - O campo _usuario_ é obrigatório. Ele deve ter ao menos 5 caracteres e no máximo 10.
 - O campo _senha_ é obrigatório.

O método **autenticar** na aplicação deve verificar na base de dados dentro do arquivo **dados.py** da aplicação contas se o usuário existe e, caso exista, se a senha está correta. Caso um deles não esteja certo, deve lançar o erro de formulário: "Usuário ou senha incorretos!" e devolver False. Se houver, deve devolver True.

#### Esqueci
O formulário deve estar associado à página de esqueci a senha na aplicação **contas**. Além disso deve validar:
 
 - O campo _git@github.com:Prof-YuriDirickson/minilms-mvc.git
email_ é obrigatório.

O método **enviar_senha** deve verificar se o e-mail está cadastrado na base **dados.py**, se não estiver deve devolver um erro de formulário "E-mail não cadastrado!". Se existir, deve mandar um e-mail com os seguintes dados:
 - Assunto: FIT Contato - Lembre de Senha
 - E-mail Destino: O e-mail digitado pelo usuário
 - E-mail Origem: contato@fit.com.br
 - Mensagem: A senha do seu usuário é {{ SENHA }} (substituir {{ SENHA }} pela senha da base)

 #### Lembrar

 O formulário deve estar associado à página de lembrar a senha da aplicação **contas**. Ele deve validar:

 - O campo _senha_ é obrigatório.
 - O campo _confirmacao_senha_ é obrigatório.

O método **salvar_senha** deve verificar se as senhas estão iguais. Se não estiverem, deve voltar um erro de formulário "Senhas devem ser iguais!".

#### Inscrever
 O formulário deve estar associado à página de inscrição da aplicação **contas**. Ele deve validar:
 - O campo _usuario_ é obrigatório e deve ter de 5 a 10 caracteres.
 - O campo _senha_ é obrigatório.
 - O campo _confirmacao-senha_ é obrigatório.
 - O campo _nome_ é completo e deve de 5 a 100 caracteres.
 - O campo _email_ é obrigatório e deve ser um e-mail válido.
 - O campo _celular_ não é obrigatório.
 - O campo _sexo_ é obrigatório e deve permitir apenas uma opção (F/M).
 - O campo _cor_ não é obrigatório.
 - O campo _github_ não é obrigatório, mas deve aceitar URL's válidas apenas.

O método **inscrever** deve verificar os seguintes dados extras:
 - Se o usuário já existe ou não na base **dados.py** (Erro: Usuário já existe!).
 - Se as senhas digitadas são iguais (Erro: Senhas devem ser iguais!).
 - Se o e-mail já está cadastrado (Erro: Já existe usuário com este e-mail!).

Se passar em tudo, deve registrar o novo usuário na base.

### CRUD Completo

Por último, deve ser criado o cadastro do modelo Curso no sistema. para isso, vamos criar uma 2 páginas: uma para criar/alterar o curso e outra para ver os detalhes.

Para isso preenchar as views no arquivos **views.py** da aplicação cursos com a lógica necessária. Crie os mapemantos de URL's para essas páginas conforme descrito a seguir:

 - **/cursos/form/novo/** (_cursos:inserir_): Chama o formulário de inserção de cursos.
 - **/cursos/form/<sigla>/** (_cursos:alterar_): Chama o formulário de alteração do curso especificado pela sigla da URL.
 - **/cursos/<sigla>/** (_cursos:detalhes_): Chama a página de visualização do curso especificado pela sigla da URL.

Para as páginas funcionarem, construa dois novos templates: _curso.html_ (para a página de detalhes de curso) e _curso-form.html_ (para a página de inserção/alteração do curso).

Toda vez que passar no contexto um curso (pegando pela sigla), utilize o nome de atributo **curso**.

O menu da aplicação já foi alterado para levar em conta os cursos inseridos no banco de dados (veja o arquivo **context_processors.py**).

#### Model

O modelo do curso deve ter os seguintes campos:
 - Nome (até 100 caracteres, não nulo, único).
 - Sigla (até 5 caracteres, não nulo, único).
 - Ementa (texto sem limite, nulo).
 - Semestres (inteiro, não nulo).
 - Coordenador (até 120 caracteres, nulo).

#### Form

Esse formulário deve estar na _view_ de alteração/inserção e deve basicamente validar as regras do modelo e permitir salvar um novo Curso.