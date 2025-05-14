from kivy.app import App
from kivy.lang import Builder
import requests
from bannervenda import BannerVenda
from telas import *
from botoes import *

GUI = Builder.load_file("main.kv")


class MainApp(App):
    id_usuario = 1

    def build(self):
        return GUI

    def on_start(self):
        # pegar informações do usuário
        requisicao = requests.get(f"https://projetoapp-64657-default-rtdb.firebaseio.com/{self.id_usuario}.json")
        requisicao_dic = requisicao.json()

        # preencher foto de perfil
        avatar = requisicao_dic["avatar"]
        foto_perfil = self.root.ids["fotos_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

        # preencher lista de vendas
        try:
            vendas = requisicao_dic["vendas"][1:]
            for venda in vendas:
                banner = BannerVenda(cliente=venda["cliente"], foto_cliente=venda["foto_cliente"],
                                     produto=venda["produto"], foto_produto=venda["foto_produto"],
                                     data=venda["data"], preco=venda["preco"],
                                     unidade=venda["unidade"], quantidade=venda["quantidade"],)
                pagina_homepage = self.root.ids["homepage"]
                lista_vendas = pagina_homepage.ids["lista_vendas"]
                lista_vendas.add_widget(banner)
        except:
            pass

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela


MainApp().run()
