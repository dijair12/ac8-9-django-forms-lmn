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

