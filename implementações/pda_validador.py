import time

class AutomatoDePilha:
    def __init__(self):
        self.estado_atual = 'q0'
        self.pilha = ['#']  # fundo da pilha
        
    def exibir_passo(self, caractere_lido, acao_pilha):
        print(f"{self.estado_atual} --> caractere atual: '{caractere_lido}' pilha: {''.join(self.pilha)}  ação: {acao_pilha}")
        time.sleep(0.3)

    def processar(self, entrada):
        print(f"\nvalidando a entrada: {entrada}\n")
        print(f"passo a passo: {entrada}\n")
        
        for char in entrada:
            estado_anterior = self.estado_atual
            acao = ""
            
            #usando a palavra RAIOS
            if self.estado_atual == 'q0' and char == 'R':
                self.estado_atual = 'q1'; acao = "avança"
            elif self.estado_atual == 'q1' and char == 'A':
                self.estado_atual = 'q2'; acao = "avança"
            elif self.estado_atual == 'q2' and char == 'I':
                self.estado_atual = 'q3'; acao = "avança"
            elif self.estado_atual == 'q3' and char == 'O':
                self.estado_atual = 'q4'; acao = "avança"
            elif self.estado_atual == 'q4' and char == 'S':
                self.estado_atual = 'q5'; acao = "avançando pro miolo"
                
            #(q5) empilha e desempilha
            elif self.estado_atual == 'q5':
                if char == '(':
                    self.pilha.append('X'); acao = "empilhando X"
                elif char == '[':
                    self.pilha.append('Y'); acao = "empilhando Y"
                elif char == ')':
                    if self.pilha[-1] == 'X':
                        self.pilha.pop(); acao = "desempilhando X"
                    else:
                        self.estado_atual = 'q_reject'; acao = "erro de fechamento )"
                elif char == ']':
                    if self.pilha[-1] == 'Y':
                        self.pilha.pop(); acao = "desempilhando Y"
                    else:
                        self.estado_atual = 'q_reject'; acao = "erro de fechamento ]"
                elif char == 'E':
                    self.estado_atual = 'q6'; acao = "avança para sufixo"
                else:
                    self.estado_atual = 'q_reject'; acao = "caractere Inválido"

            # transições do 'ND' (q6 -> q7 -> q8)
            elif self.estado_atual == 'q6' and char == 'N':
                self.estado_atual = 'q7'; acao = "avança"
            elif self.estado_atual == 'q7' and char == 'D':
                self.estado_atual = 'q8'; acao = "avança"
                
            else:
                self.estado_atual = 'q_reject'
                acao = "REJEITA --> transição inexistente"

            self.exibir_passo(char, acao)
            
            if self.estado_atual == 'q_reject':
                print("\nREJEITA --> erro de sintaxe ou desbalanceamento.")
                return False

        #(q8 para q_accept se a pilha estiver vazia até o fundo)
        if self.estado_atual == 'q8' and self.pilha == ['#']:
            self.estado_atual = 'q_accept'
            print("\nACEITA --> sintaxe íntegra e balanceada")
            return True
        else:
            print("\nREJEITA --> pilha não vazia ou término prematuro")
            return False

#Execução
if __name__ == "__main__":
    pda = AutomatoDePilha()
    pda.processar("RAIOS([()])END") #Aceita
    
    print("\n" + "="*40)
    pda2 = AutomatoDePilha()
    pda2.processar("RAIOS([)]END")   #Rejeita