'''Exercício – Particionamento em Classes de Equivalência e Análise do Valor Limite

2) Desenvolva um caso de uso de incluir contato em uma agenda telefônica. Os dados de um contato são: Nome, Telefone, email. A inclusão do contato deve seguir as seguintes regras:
    a. Todo contato deve possuir um número telefônico
    b. Não pode haver dois contatos com o mesmo número telefônico
    c. Um número telefônico deve ter entre 8 e 15 dígitos numéricos
    d. Cada contato tem que possuir um email no formato alfanumérico e deve seguir a regra de formatação "texto@domínio.extensão", onde "texto" pode conter letras e/ou números; "domínio" deve conter letras.
** Elabore os casos de testes necessários para este caso de uso.'''

agenda = []

def incluir_contato(nome, telefone, email):
    # Validação do telefone
    if telefone is None or not str(telefone).isdigit():
        raise ValueError("INVÁLIDO: O contato deve possuir um número telefônico apenas com dígitos.")
    if len(str(telefone)) < 8:
        raise ValueError("INVÁLIDO: O número telefônico deve ter entre 8 e 15 dígitos.")
    if len(str(telefone)) > 15:
        raise ValueError("INVÁLIDO: O número telefônico deve ter entre 8 e 15 dígitos.")
    for contato in agenda:
        if contato['telefone'] == telefone:
            raise ValueError("INVÁLIDO: Já existe um contato com esse número telefônico.")

    # Validação do email
    import re
    email_regex = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]$'
    if not re.match(email_regex, email):
        raise ValueError("INVÁLIDO: O email deve estar no formato texto@dominio.extensão e seguir as regras de formatação.")

    # Adiciona contato se tudo estiver válido
    agenda.append({'nome': nome, 'telefone': telefone, 'email': email})
    return "VÁLIDO: Contato adicionado com sucesso."

