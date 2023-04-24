import openai
import tkinter as tk

def armazenando_texto():
   global texto
   texto = caixa_texto.get()
   root.quit()

root = tk.Tk()
root.geometry('300x100')
caixa_texto = tk.Entry(root, width = 30)
caixa_texto.pack(fill = tk.X, padx = 10, pady=10)

botao = tk.Button(root, text = "Enviar mensagem", command = armazenando_texto)
botao.pack()
root.mainloop()


root.update()
if texto:
    openai.api_key = "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"
    pre_prompt = "Você é um avaliador de redação oficial do ENEM. O tema da redação é feminismo Dê uma nota de 0 a 1000 para essa redação abaixo, seja rigoroso. Considerando os seguintes criterios: 1. Domínio da escrita formal em língua portuguesa, 2. Compreensão do tema e aplicação das áreas de conhecimento, 3. Capacidade de interpretação das informações e organização dos argumentos, 4. Domínio dos mecanismos linguísticos de argumentação, 5. Capacidade de conclusão com propostas coerentes que respeitem os direitos humanos.Leve em consideração que o tema da redação é feminismo. E depois disso cite os pontos positivos e negativos e o que tem a melhorar"
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