import requests
import persistencia
 
def mostrar_clima():
    cidade = input('Digite a cidade que deseja ver o clima: ').strip()

    while cidade == '':
        print('Por favor, digite uma cidade válida.')
        cidade = input('Digite a cidade que deseja ver o clima: ').strip()

    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&units=metric&lang=pt_br&appid=7442cc5859d171c2e7c7be34b0be973e'
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        clima = dados['weather'][0]['description']
        temperatura = dados['main']['temp']
        print(f'Clima em {cidade}: {clima.capitalize()}')
        print(f'Temperatura: {temperatura}°C')

        persistencia.salvar_historico(cidade)

    except requests.exceptions.HTTPError as e:
        print(f'Erro HTTP: {e}')

    except requests.exceptions.RequestException as e:
        print(f'Erro de conexão: {e}')
    
    except KeyError:
        print('Cidade não encontrada.')


def ver_historico():
    historico = persistencia.ler_historico()
    print('Histórico de cidades consultadas:')

    for cidade in historico:
        print(cidade)

    if not historico:
        print('Nenhuma cidade consultada ainda.')


def menu():
    while True:
        print('1 - Ver clima')
        print('2 - Ver histórico')
        print('3 - Sair')

        try:
            escolha = int(input('Escolha uma opção: '))

            if escolha == 1:
                mostrar_clima()
            elif escolha == 2:
                ver_historico()
            elif escolha == 3:
                print('Tchau!')
                break

            if escolha not in [1, 2, 3]:
                print('Por favor, escolha uma opção válida.')
                continue    
    
        except ValueError:
            print('Por favor, escolha uma opção válida.')

if __name__ == '__main__':
    menu()