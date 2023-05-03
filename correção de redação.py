import openai
import tkinter as tk

def armazenando_texto():
   global texto
   texto = caixa_texto.get()
   root.quit()

root = tk.Tk()
root.geometry('600x600')
caixa_texto = tk.Entry(root, width = 30)
caixa_texto.pack(fill = tk.X, padx = 10, pady=10)

botao = tk.Button(root, text = "Nota da sua redação", command = armazenando_texto)
botao.pack()
root.mainloop()


root.update()
if texto:
    openai.api_key = "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"
    pre_prompt = "Você é um avaliador de redação oficial do ENEM cujo tema é Feminicidio no Brasil, se a redação não tiver nada haver com o tema ela devera ser desconsiderada. Dê uma nota de 0 a 1000 para a redação seguindo as competências cobradas na redação do enem, seja rigoroso. Considerando os seguintes criterios: 1. Domínio da escrita formal da língua portuguesa, 2. Compreender o tema e não fugir do que é proposto, 3. Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista, 4. Conhecimento dos mecanismos linguísticos necessários para a construção da argumentação, 5. Respeito aos direitos humanos. Leve em consideração que o tema da redação é feminicidio. E depois disso cite os pontos positivos e negativos e o que tem a melhorar."
    solicitacao = texto
    pos_prompt = "\nA nota para essa redação é:"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= pre_prompt + solicitacao + pos_prompt,
      temperature=0.6,
      max_tokens=2000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
print(response.choices[0].text)
texto = ''   