import time

class MTMulfitita:
    def __init__(self, entrada1, entrada2):
        self.fita1 = list(entrada1) + ['_'] * 5
        self.fita2 = list(entrada2) + ['_'] * 5
        self.fita3 = ['_'] * len(self.fita1)
        self.cabeca1 = self.cabeca2 = self.cabeca3 = 0
        self.estado = 'q0'

    def imprimir_fitas(self):
        def formatar_fita(fita, cabeca):
            fita_str = ""
            for i, val in enumerate(fita):
                if i == cabeca:
                    fita_str += f"[{val}] "
                else:
                    fita_str += f" {val}  "
            return fita_str.strip()

        print(f"Estado: {self.estado}")
        print(f"Fita 1: {formatar_fita(self.fita1, self.cabeca1)}")
        print(f"Fita 2: {formatar_fita(self.fita2, self.cabeca2)}")
        print(f"Fita 3: {formatar_fita(self.fita3, self.cabeca3)}")
        print("-" * 40)
        time.sleep(0.4)

    def processar(self):
        print("iniciando leitor de fitas:\n")
        self.imprimir_fitas()

        while self.estado not in ['q_accept', 'q_reject']:
            lido1 = self.fita1[self.cabeca1]
            lido2 = self.fita2[self.cabeca2]

            #q0 e q1 validam a header 'HD'
            if self.estado == 'q0' and lido1 == 'H' and lido2 == 'H':
                self.estado = 'q1'
                self.cabeca1 += 1; self.cabeca2 += 1; self.cabeca3 += 1
            elif self.estado == 'q1' and lido1 == 'D' and lido2 == 'D':
                self.estado = 'q2'
                self.cabeca1 += 1; self.cabeca2 += 1; self.cabeca3 += 1
            
            #q2 Processa os dados (0 ou 1) e desvia para estados temporários q3/q4 pra escrever
            elif self.estado == 'q2':
                if lido1 == '0' and lido2 == '0':
                    self.estado = 'q3'
                elif lido1 == '1' and lido2 == '1':
                    self.estado = 'q4'
                elif lido1 == 'F' and lido2 == 'F':
                    self.estado = 'q5' #avança pra validar o footer
                else:
                    self.estado = 'q_reject'
            
            #q3 escreve 0 na fita 3 e volta para q2
            elif self.estado == 'q3':
                self.fita3[self.cabeca3] = '0'
                self.estado = 'q2'
                self.cabeca1 += 1; self.cabeca2 += 1; self.cabeca3 += 1

            #q4 escreve 1 na fita 3 e volta para q2
            elif self.estado == 'q4':
                self.fita3[self.cabeca3] = '1'
                self.estado = 'q2'
                self.cabeca1 += 1; self.cabeca2 += 1; self.cabeca3 += 1

            #q5 e q6 validam footers 'FN' e aceitam se ambos baterem
            elif self.estado == 'q5':
                self.cabeca1 += 1; self.cabeca2 += 1; self.cabeca3 += 1
                self.estado = 'q6'
            elif self.estado == 'q6' and lido1 == 'N' and lido2 == 'N':
                self.fita3[self.cabeca3] = 'V' #V de válido
                self.estado = 'q_accept'
            else:
                self.estado = 'q_reject'

            self.imprimir_fitas()

        if self.estado == 'q_accept':
            print("\nACEITA --> fluxos sincronizados e transferidos")
        else:
            print("\nREJEITA --> divergência de dados, cabeçalho incorreto ou caractere inválido")

#Execução
if __name__ == "__main__":
    mt = MTMulfitita("HD1010FN", "HD1010FN") # Aceito
    mt.processar()