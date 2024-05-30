queue = []

def add_number(number):
    queue.insert(0, number)

def delete_number():
    if queue:
        queue.pop()
    else:
        print("A fila está vazia. Não é possível excluir.")

def show_queue():
    if queue:
        print("Fila:", queue)
    else:
        print("A Fila está vazia")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar numero")
        print("2. Excluir numero")
        print("3. Mostrar fila")
        print("4. Sair")

        choice = input("Escolha um opção: ")

        if choice == '1':
            number = int(input("Digite um numero: "))
            add_number(number)
            show_queue()

        elif choice == '2':
            delete_number()
            show_queue()

        elif choice == '3':
            show_queue()

        elif choice == '4':
            print("Saindo...")
            break

        else:
            print("Opção Invalida. Escolha outra opção.")

menu()