import pandas as pd
from flask import Flask

tabela = pd.read_csv("dados.csv")

print("Colunas no CSV:", tabela.columns)
print(tabela)

arq_html = 'index.html'

laurinha = Flask(__name__)
@laurinha.route("/")
def pagina():
    html = "<h1>Acompanhamento do Status das Esteiras - Monitoramento de Estoque</h1><br>\n"

    for index, linha in tabela.iterrows():
        date = linha["Date"]
        time = linha["Time"]
        esteira1 = ''
        esteira2 = ''
        esteira3 = ''

        if linha["esteira1"] == 2:
            esteira1 +=  "🟢"
        elif linha["esteira1"] == 1:
            esteira1 += "🟡"
        else:
            esteira1 +=  "🔴"

        if linha["esteira2"] == 2:
            esteira2 +=  "🟢"
        elif linha["esteira2"] == 1:
            esteira2 += "🟡"
        else:
            esteira2 +=  "🔴"

        if linha["esteira3"] == 2:
            esteira3 +=  "🟢"
        elif linha["esteira3"] == 1:
            esteira3 += "🟡"
        else:
            esteira3 +=  "🔴"

        html += f"<p><strong>{date}</strong> <strong>{time}</strong> : Esteira 1: {esteira1} | Esteira 2: {esteira2} | Esteira 3: {esteira3}</p>"

    with open(arq_html, 'w', encoding='utf-8') as pagina_criada:
        pagina_criada.write(f"<html>\n"
                            f"<body>\n"
                            f"{html}\n"
                            f"</body>\n"
                            f"</html>")
        print("Feito!")

    return html

pagina()

laurinha.run(debug=True)