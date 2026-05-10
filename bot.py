import requests
import time
memoria = {}

TOKEN = "8772436120:AAGYul1_h-5thzeB8iyQ9BmehaBDy61eSeI"

url_base = f"https://api.telegram.org/bot{TOKEN}"

ultimo_update = None

print("Bot conversacional iniciado...")

while True:

    resposta = requests.get(url_base + "/getUpdates").json()

    if resposta["result"]:

        for update in resposta["result"]:

            update_id = update["update_id"]

            if ultimo_update is None or update_id > ultimo_update:

                ultimo_update = update_id

                if "message" not in update:
                    continue

                mensagem = update["message"]["text"].lower()

                chat_id = update["message"]["chat"]["id"]

                # SAUDAÇÃO
                if (
                    "oi" in mensagem
                    or "olá" in mensagem
                    or "bom dia" in mensagem
                ):

                    resposta_texto = (
                        "Olá 😊\n"
                        "Como posso ajudar?\n\n"
                        "• Agendamentos\n"
                        "• Procedimentos\n"
                        "• Valores"
                    )

                # AGENDAMENTO
                elif (
                    "agendar" in mensagem
                    or "horário" in mensagem
                    or "marcar" in mensagem
                ):

                    resposta_texto = (
                        "Claro 😊\n"
                        "Qual dia você gostaria de agendar?"
                    )

                # PREÇO
                elif (
                    "preço" in mensagem
                    or "valor" in mensagem
                    or "custa" in mensagem
                ):

                    resposta_texto = (
                        "Nossos procedimentos começam a partir de R$100 😊"
                    )

                # PROCEDIMENTOS
                elif (
                    "botox" in mensagem
                    or "limpeza" in mensagem
                    or "peeling" in mensagem
                ):

                    resposta_texto = (
                        "Temos vários procedimentos disponíveis 😊"
                    )

                # NÃO ENTENDEU
                else:

                    resposta_texto = (
                        "Desculpe 😊\n"
                        "Ainda não entendi sua mensagem."
                    )

                requests.post(
                    url_base + "/sendMessage",
                    data={
                        "chat_id": chat_id,
                        "text": resposta_texto
                    }
                )

    time.sleep(2)
