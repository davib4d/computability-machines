import time

class AutomatoDePilha:
    def __init__(self):
        self.estado_atual = 'q0'
        self.pilha = ['$']  # fundo da pilha
        
    def exibir_passo(self, caractere_lido, acao_pilha):
        print(f"[{self.estado_atual}] Lendo: '{caractere_lido}' | Pilha: {''.join(self.pilha)} | Ação: {acao_pilha}")
        time.sleep(0.3)

    def processar(self, entrada):
        print(f"\n--- Iniciando Validação PDA ---")
        print(f"Entrada: {entrada}\n")
        
        for char in entrada:
            estado_anterior = self.estado_atual
            acao = ""
            
            #'BEGIN' (q0 -> q1 -> q2 -> q3 -> q4 -> q5)
            if self.estado_atual == 'q0' and char == 'B':
                self.estado_atual = 'q1'; acao = "Avança"
            elif self.estado_atual == 'q1' and char == 'E':
                self.estado_atual = 'q2'; acao = "Avança"
            elif self.estado_atual == 'q2' and char == 'G':
                self.estado_atual = 'q3'; acao = "Avança"
            elif self.estado_atual == 'q3' and char == 'I':
                self.estado_atual = 'q4'; acao = "Avança"
            elif self.estado_atual == 'q4' and char == 'N':
                self.estado_atual = 'q5'; acao = "Avança para Miolo"
                
            #(q5) empilha e desempilha
            elif self.estado_atual == 'q5':
                if char == '(':
                    self.pilha.append('X'); acao = "Empilha X"
                elif char == '[':
                    self.pilha.append('Y'); acao = "Empilha Y"
                elif char == ')':
                    if self.pilha[-1] == 'X':
                        self.pilha.pop(); acao = "Desempilha X"
                    else:
                        self.estado_atual = 'q_reject'; acao = "Erro de Fechamento )"
                elif char == ']':
                    if self.pilha[-1] == 'Y':
                        self.pilha.pop(); acao = "Desempilha Y"
                    else:
                        self.estado_atual = 'q_reject'; acao = "Erro de Fechamento ]"
                elif char == 'E':
                    self.estado_atual = 'q6'; acao = "Avança para Sufixo"
                else:
                    self.estado_atual = 'q_reject'; acao = "Caractere Inválido"

            # Transições do Sufixo 'ND' (q6 -> q7 -> q8)
            elif self.estado_atual == 'q6' and char == 'N':
                self.estado_atual = 'q7'; acao = "Avança"
            elif self.estado_atual == 'q7' and char == 'D':
                self.estado_atual = 'q8'; acao = "Avança"
                
            else:
                self.estado_atual = 'q_reject'
                acao = "Rejeitado - Transição Inexistente"

            self.exibir_passo(char, acao)
            
            if self.estado_atual == 'q_reject':
                print("\n[RESULTADO] Cadeia REJEITADA: Erro de sintaxe ou desbalanceamento.")
                return False

        #(q8 para q_accept se a pilha estiver vazia até o fundo)
        if self.estado_atual == 'q8' and self.pilha == ['$']:
            self.estado_atual = 'q_accept'
            print("\n[RESULTADO] Cadeia ACEITA: Sintaxe íntegra e balanceada!")
            return True
        else:
            print("\n[RESULTADO] Cadeia REJEITADA: Pilha não vazia ou término prematuro.")
            return False

#Execução
if __name__ == "__main__":
    pda = AutomatoDePilha()
    pda.processar("BEGIN([()])END") #Aceita
    
    print("\n" + "="*40)
    pda2 = AutomatoDePilha()
    pda2.processar("BEGIN([)]END")   #Rejeita