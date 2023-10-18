Este projeto tem como objetivo aprimorar o monitoramento realizado com a ferramenta Zabbix.

Através da sua API, o projeto recupera os hosts existentes que têm problemas e gera uma janela de notificação com:

Nome do host
Nome do problema
Horário do problema

Sim, a ferramenta Zabbix já oferece funcionalidades semelhantes, no entanto, são relativamente limitadas em relação à monitoria de redes.

Este projeto continuará registrando problemas enquanto eles existirem, a menos que tenham sido reconhecidos, suprimidos ou reconectados/recuperados.

Por questões de privacidade, o arquivo login_user.py foi adicionado para ser ignore.

Exemplo de implementação:
Dentro da pasta ext, adicione o arquivo chamado login_user.py ou o nome de sua escolha.

from zabbix_api import ZabbixAPI

def get_token():
auth_token = "SEU TOKEN AQUI"
    return auth_token

def get_urlZabbix():
api_url = '"SEU CAMINHO DO ZABBIX"/api_jsonrpc.php'
    return api_url

def login_user_zabbix():
URL = "SEU CAMINHO DO ZABBIX"
USERNAME = "SEU USUÁRIO AQUI"
PASSWORD = "SUA SENHA AQUI"

    try:
        zapi = ZabbixAPI(URL, timeout=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'Conectado à API do Zabbix, versão {zapi.api_version}')
    except Exception as erro:
        print(f'Não foi possível conectar à API do Zabbix! {erro}')
        exit()
    return zapi


Lembre-se de substituir o que está dentro das aspas duplas ("") pelos seus dados de login e token.

Para baixar as bibliotecas, você pode executar o comando "pip freeze" diretamente no terminal do repositório para listar as bibliotecas e instalá-las.

Para alterar a gravidade dos problemas, siga os caminhos:

problems.py - def problems_from_severity(host_info): Altere onde estiver "severities": Número da gravidade.

hosts_problems.py - def make_api_request(): Altere onde estiver "severities": Número da gravidade.



Obrigado.

Novas atualizações virão com o tempo.
