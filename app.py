from model import model_lead
import control




def add_lead():
    name = input('Nome: ')
    email = input('E-mail: ')
    stage = input('Etapa no Funil: ')

    # validar os dados. . .
    # depois de validar os dados precisamos modelar o lead como um dict
    # usaremos o model para isso
    print(model_lead(name,email,stage))

    #usar control
    control.create_lead((model_lead(name,email,stage)))

def main():
    while True:
        print('\n Mini CRM de Leads')
        print('1- Adicionar Leads')
        print('2- Listar Leads')
        print('0- Sair do programa')

        opt = input('Escolha uma opção: ')

        if opt == '1':
            add_lead()
        elif opt == '2':
            list_leads()
        elif opt == '0':
            print('Até mais')
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()