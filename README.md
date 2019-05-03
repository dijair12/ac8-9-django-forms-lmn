# Exercício Django MVC

# Enunciado
Nessa atividade será criada a primeira estrutura de um projeto Django, aproveitando as melhores práticas do Django vistas em aula e do padrão MVC de projetos.

## Como começar
Logo após a clonagem desse respositório, você deve criar um ambiente virtual do Python, instalar o Django e iniciar o projeto do Django nessa mesma pasta (na raiz).

Não esqueça de commitar no repositório o arquivo *requirements.txt*, ele é necessário para rodar os testes.

Depois de criar o projeto Django, migre os arquivos de testes paras áreas correspondentes de cada um.

## Instruções Técnicas

O conteúdo estático do site foi movido para a pasta **estatico** no projeto. Esse conteúdo deve ser migrado para dentro do projeto Django respeitando a alocação em aplicações.

### Arquivos Teste
Ao criar o projeto do Django, na pasta principal você deve copiar o arquivo *testes_projeto.py* para dentro dessa pasta. 

Os demais arquivos teste devem estar dentro da aplicação correspondente.

Em todos os casos, renomeie os arquivos para *tests.py* após a cópia.

### Aplicações

Após isso devem ser criados as seguintes aplicações e as páginas dentro delas:

 - **website**: aplicação do conteúdo principal do site, além do conteúdo estático compelto (páginas index e contato) .
 - **contas**: aplicação que gerencia as contas, login e autorização (páginas login, inscrever, lembrar e esqueci).
 - **cursos**: aplicação que gerencia os cursos e dsiciplinas da faculdade (páginas ads, bd, gti, si).
 - **restrito**: aplicação que cuidará da área restrita do LMS (página notas).

### Páginas

Cada uma das páginas deve responder a um **caminho de url** e a uma **url nomeada** específicos. Aleḿ disso todos os *templates* devem estender de um básico (chamado de *base.html*), onde nesse *template* estará todo o conteúdo HTML fora da tamain (head, footer e header).

Lembre-se que uma **url nomeada** deve acompanhar o *namespace* da sua aplicação

#### index.html
 - *URL*: /
 - *URL NOMEADA*: website:home
 
#### contato.html
 - *URL*: /contato/
 - *URL NOMEADA*: website:contato

#### esqueci.html
 - *URL*: /esuqeci-a-senha/
 - *URL NOMEADA*: contas:esqueci

#### lembrar.html
 - *URL*: /lembrar/
 - *URL NOMEADA*: contas:lembrar

#### inscrever.html
 - *URL*: /inscrever
 - *URL NOMEADA*: contas:inscrever

#### login.html
 - *URL*: /entrar/
 - *URL NOMEADA*: contas:entrar

#### notas.html
 - *URL*: /restrito/notas/
 - *URL NOMEADA*: restrito:notas

#### ads.html
 - *URL*: /cursos/ads/
 - *URL NOMEADA*: cursos:ads

#### bd.html
 - *URL*: /cursos/bd/
 - *URL NOMEADA*: cursos:bd

#### gti.html
 - *URL*: /cursos/gti/
 - *URL NOMEADA*: cursos:gti

#### si.html
 - *URL*: /cursos/si/
 - *URL NOMEADA*: cursos:si

## Regras

A nota será dada de acordo com a quantidade de testes que passarem ao entregar esse exercício. Alguns critérios não obedecidos são eliminatórios (nota 0):

- Ausência do arquivo *requirements.txt* com a versão do Django utilizada
- O projeto Django não foi criado na raiz (basta ver se o arquivo *manage.py* está na raiz)
- Se os arquivos de teste base não forem devidamente copiados ao seus lugares corretos.

Preste atenção nos *namespaces* definidos nas instruções, eles devem ser obedecidos para os testes passarem. Da mesma forma, os caminhos de URL.

### Contato

O formulário de contato deve conseguir mandar um e-mail a um endereço específico. O Django possui uma maneira própria de envio de e-mail (veja aqui: https://docs.djangoproject.com/pt-br/2.2/topics/email/). Podem usar a versão de **console** de envio de e-mail.

O e-mail deve ser enviado com as seguintes regras:
 - O assunto (*subject*) deve ser **FIT Contato -  {{ ASSUNTO }}**, onde o **{{ ASSUNTO }}** é o assunto escolhido pelo usuário ao preencher o formulário de contato (Bug, Reclamação ou Sugestão).
 - O e-mail remetente deve ser o que o usuário digitou no formulário.
 - O e-mail destinatário deve ser *contato@fit.com.br*.
 - Os tipos de resposta devem vir como o nome inteiro, T para Telefone e E para E-mail.
 - O texto do e-mail deve estar no seguinte formato:
 ```
 Você recebeu o contato do seguinte usuário:
 ->Nome: {{ NOME DIGITADO PELO USUÁRIO }}
 ->E-mail: {{ EMAIL DIGITADO PELO USUÁRIO }}
 ->Telefone: {{ TELEFONE DIGITADO PELO USUÁRIO }}
 ->Assunto: {{ ASSUNTO ESCOLHIDO PELO USUÁRIO }}
 ->Resposta: {{ TIPOS DE RESPOSTA ESCOLHIDOS PELO USUÁRIO (separados por ;) }}
 ->Mensagem: {{ MENSAGEM DIGITADA PELO USUÁRIO }}
 ´´´
