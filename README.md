# Exercício Django Formulários

# Enunciado
Nessa atividade serão criados os formulários no Django, para validação e primeiras regras de negócio.

## Como começar
Após a clonagem, vocês devem fazer os formulários e testá-los. Tanto os testes quanto a maioria dos formulários HTML já estão prontos.

Vocês devem apenas programar os formulários e conectá-los às _views_ correspondentes.

## Instruções Técnicas

As classes dos formulários estão criadas nas suas respectivas aplicações. Vocês devem apenas preencher os campos e os métodos necessários.

### Formulários

Devem ser criados os formulários citados abaixo, cada um com sua respectiva página. Os formulários devem validar conforme as regras apresentadas.

#### Contato

Esse formulário deve estar associado à página de contato na aplicação **website**. Ele deve coletar os campos iguais ao formulário HTML e fazer as seguintes validações:
 
 - O campo _nome_ é obrigatório e deve ter no máximo 120 caracteres.
 - O campo _email_ só é obrigatório se o tipo de resposta incluir e-mail. Caso o e-mail esteja preenchido, ele deve ser válido
 - O campo _telefone_ só é obrigatório se o tipo de resposta incluir telefone.
 - O campo _assunto_ é obrigatório e deve verificar se o escolhido foi uma das três opções válidas (B,R ou S).
 - O campo _mensagem_ é obrigatório.
 - O campo _resposta_ não é obrigatório.


#### Entrar
O formulário deve estar associado à página de login na aplicação **contas**. Além disso deve validar:
 
 - O campo _usuario_ é obrigatório. Ele deve ter ao menos 5 caracteres e no máximo 10.
 - O campo _senha_ é obrigatório.

#### Esqueci
O formulário deve estar associado à página de esqueci a senha na aplicação **contas**. Além disso deve validar:
 
 - O campo _email_ é obrigatório.

### Views

Após a criação dos formulários, vocês devem conectá-los com as suas devidas views e executar uma ação adicional para cada um deles.

#### Contato

A _view_ de contato deve enviar um e-mail (no exato mesmo modelo do anterior) caso o formulário esteja válido. O método de envio de e-mail deve ser transferido para dentro do formulário.

#### Entrar

A _view_ deve tentar autenticar o usuário caso o formulário esteja válido. O método *autenticar* do formulário devolve um booleano caso consiga ou não autenticar. Caso ele volte **True**, a view deve redirecionar para a homepage do sistema. Caso contrário deve ficar na página de login mesmo.

#### Esqueci

A _view_ deve enviar um e-mail ao usuário no e-mail passado com o assunto **FIT Contato - Nova Senha** o seguinte texto:

```
Olá, você solicitou um link para gerar uma nova senha, por favor entre no seguinte link com para gerar sua nova senha: {{ LINK_LEMBRAR }}
´´´