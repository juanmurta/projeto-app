import requests
from kivy.app import App


class MyFirebase():
    API_KEY = 'AIzaSyB4FJ4vnzxfri5wydwUbfMnhz9r1BMrdMs'

    def criar_conta(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        info = {
            "email": email,
            "password": senha,
            "returnSecureToken": True
        }
        requisicao = requests.post(link, data=info)
        requisicao_dic = requisicao.json()

        if requisicao.ok:
            print("Conta criada com sucesso!")
            refresh_token = requisicao_dic["refreshToken"]
            local_id = requisicao_dic["localId"]
            id_token = requisicao_dic["idToken"]

            meu_aplicativo = App.get_running_app()
            meu_aplicativo.local_id = local_id
            meu_aplicativo.id_token = id_token

            with open("refreshtoken.txt", "w") as arquivo:
                arquivo.write(refresh_token)

            link = "https://projetoapp-64657-default-rtdb.firebaseio.com/{local_id}.json"
            info_usuario = '{"avatar": "foto7.png", "equipe": "", "total_vendas": "0", "vendas": ""}'
            requisicao_usuario = requests.patch(link, data=info_usuario)

            meu_aplicativo.carregar_infos_usuario()
            meu_aplicativo.mudar_tela("homepage")

        else:
            mensagem_erro = requisicao_dic['error']['message']
            meu_aplicativo = App.get_running_app()
            pagina_login = meu_aplicativo.root.ids["loginpage"]
            pagina_login.ids["mensagem_login"].text = mensagem_erro
            pagina_login.ids["mensagem_login"].color = (1, 0, 0, 1)
        print(requisicao_dic)

    def fazer_login(self, email, senha):
        link = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}"
        info = {
            "email": email,
            "password": senha,
            "returnSecureToken": True
        }
