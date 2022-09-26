while True: 
    try: 
           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
           # e imprima a saída de acordo com a situação das pernas do papagaio

            levantamento_perna = input()
            if levantamento_perna == "esquerda":
                print("ingles\n")
            elif levantamento_perna == "direita":
                print("frances\n")
            elif levantamento_perna == "nenhuma":
                print("portugues\n")
            elif levantamento_perna == "ambas":
                print("caiu")
                break
           
    except EOFError: 
        break