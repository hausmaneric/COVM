class GeradorIDSequencial:
    def __init__(self):
        self.ultimo_id = 0
    
    def gerar_id(self):
        self.ultimo_id += 1
        return self.ultimo_id