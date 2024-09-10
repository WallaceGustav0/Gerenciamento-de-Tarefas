def validar_status(status):
    status_validos = ["pendente", "em andamento", "concluida"]
    if status not in status_validos:
        print(f"Status inválido: {status}. Status válidos são {status_validos}.")
        return None
    return status


def validar_prioridade(prioridade):
    prioridades_validas = ["alta", "media", "baixa"]
    if prioridade not in prioridades_validas:
        print(f"Prioridade inválida: {prioridade}. Prioridades válidas são {prioridades_validas}.")
        return None
    return prioridade


def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    status = validar_status(status)
    prioridade = validar_prioridade(prioridade)
    if status is None or prioridade is None:
        print("Tarefa não foi adicionada devido a entradas inválidas.")
        return

    novo_id = max([tarefa['id'] for tarefa in lista_tarefas], default=0) + 1

    nova_tarefa = {
        'id': novo_id,
        'descricao': descricao,
        'status': status,
        'prioridade': prioridade
    }

    lista_tarefas.append(nova_tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")


def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("Nenhuma tarefa disponível.")
    else:
        print("\nTarefas atuais:")
        for tarefa in lista_tarefas:
            print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, "
                  f"Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")
        print()


def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = [
        tarefa for tarefa in lista_tarefas
        if (status is None or tarefa['status'] == status) and
           (prioridade is None or tarefa['prioridade'] == prioridade)
    ]
    
    if not tarefas_filtradas:
        print("Nenhuma tarefa encontrada com os filtros fornecidos.")
    else:
        print(f"\nTarefas filtradas (Status: {status}, Prioridade: {prioridade}):")
        for tarefa in tarefas_filtradas:
            print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, "
                  f"Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")
        print()
    return tarefas_filtradas


def main():
    lista_tarefas = []
    
    opcoes = {
        '1': "Adicionar tarefa",
        '2': "Visualizar todas as tarefas",
        '3': "Filtrar tarefas",
        '4': "Sair"
    }
    
    while True:
        print("\nGerenciamento de Tarefas:")
        for opcao, descricao in opcoes.items():
            print(f"{opcao}. {descricao}")
        
        opcao = input("Escolha uma opção (1, 2, 3 ou 4): ").strip()
        if opcao == '1':
            descricao = input("Descreva a tarefa: ").strip()
            status = input("Selecione o Status (pendente, em andamento, concluida): ").lower().strip()
            prioridade = input("Selecione a Prioridade (alta, media, baixa): ").lower().strip()

            adicionar_tarefa(lista_tarefas, descricao, status, prioridade)
        
        elif opcao == '2':
            visualizar_tarefas(lista_tarefas)
        
        elif opcao == '3':
            status_filtro = input("Filtrar por status (pendente, em andamento, concluida) ou deixar em branco: ").lower().strip() or None
            prioridade_filtro = input("Filtrar por prioridade (alta, media, baixa) ou deixar em branco: ").lower().strip() or None
            
            status_filtro = status_filtro if status_filtro in ["pendente", "em andamento", "concluida"] else None
            prioridade_filtro = prioridade_filtro if prioridade_filtro in ["alta", "media", "baixa"] else None
            
            filtrar_tarefas(lista_tarefas, status_filtro, prioridade_filtro)
        
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()