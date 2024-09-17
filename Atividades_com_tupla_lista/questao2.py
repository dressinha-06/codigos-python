temp = []
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

for tp in range(12):
    float(input(f"Adicione a temperatura do {tp + 1}º mês {meses[tp]}: "))

    temp.append(tp)
    print(temp) 

    
