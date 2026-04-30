import os
import json

filename = 'historico_cidades'

def salvar_historico(cidade):
    try:    
        # Salvar os dados existentes
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                historico = json.load(f)
                if not isinstance(historico, list):
                    historico = []
        else:
            historico = []
    except (json.JSONDecodeError, FileNotFoundError):
        historico = [] 

    # Para evitar duplicatas
    if cidade in historico:
        historico.remove(cidade)

    # Esse comando vai adicionar a nova cidade consultada no primeiro índice (0)
    historico.insert(0, cidade)

    # Esse comando vai limitar o histórico para 10 cidades
    historico = historico[:10]

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)


def ler_historico():
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf=8') as f:
            dados = json.load(f)
            return dados if isinstance(dados, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

    
