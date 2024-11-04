def ler_temp(mes):
    while True:
        try:
            temp = float(input(f"Digite a temperatura máxima do mês {mes}: "))
            if -60 <= temp <= 50:
                return temp
            else: #Fiz ser possível retornar ao comando para informar a temperatura correta.
                print("Temperatura fora do intervalo válido (-60 a 50 graus Celsius). Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

#Área de memória e variáveis.
def mesp_ex(mes):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return meses[mes - 1]

def main():
    temperaturas = []
    meses_es = 0
    mes_mais_quente = None
    mes_menos_quente = None

    for mes in range(1, 13): #Estrutura de repetição que aprendi a um tempo de forma autodidata.
        temp = ler_temp(mes)
        temperaturas.append(temp)

        #Área de cálculo.
        if temp > 33:
            meses_es = meses_es + 1

        if mes_mais_quente is None or temp > temperaturas[mes_mais_quente - 1]:
            mes_mais_quente = mes

        if mes_menos_quente is None or temp > temperaturas[mes_menos_quente - 1]:
            mes_menos_quente = mes

    temperatura_media_anual = sum(temperaturas) / len(temperaturas)

    #prompt de saída.
    print(f"Temperatura média máxima anual: {temperatura_media_anual:.2f} graus Celsius")
    print(f"Quantidade de meses escaldantes: {meses_es}")
    print(f"Mês mais escaldante do ano: {mesp_ex(mes_mais_quente)}")
    print(f"Mês menos quente do ano: {mesp_ex(mes_menos_quente)}")

if __name__ == "__main__":
    main()