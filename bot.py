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
                if chat_id not in memoria:
                memoria[chat_id] = {}

                estado = memoria[chat_id]
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

    if "agendamento" in mensagem.lower():

        estado["etapa"] = "esperando_dia"

        resposta_texto = "Claro! Qual dia você deseja agendar?"

    elif estado.get("etapa") == "esperando_dia":

        dia = mensagem

        estado["dia"] = dia
        estado["etapa"] = "esperando_horario"

        resposta_texto = f"Perfeito! Qual horário para {dia}?"

    elif estado.get("etapa") == "esperando_horario":

        horario = mensagem

        dia = estado.get("dia")

        resposta_texto = f"Agendamento anotado para {dia} às {horario}."

        memoria[chat_id] = {}

    else:

        resposta_texto = "Desculpe, não entendi."
