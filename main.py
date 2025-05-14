from kivy.app import App
from kivy.lang import Builder
import requests
from telas import *
from botoes import *

GUI = Builder.load_file("main.kv")


class MainApp(App):
    id_usuario = 1

    def build(self):
        return GUI

    def on_start(self):
        requisicao = requests.get(f"https://projetoapp-64657-default-rtdb.firebaseio.com/{self.id_usuario}.json")
        requisicao_dic = requisicao.json()
        avatar = requisicao_dic["avatar"]

    def mudar_tela(self, id_tela):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela


MainApp().run()
