from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Substitua 'your-slack-bot-token' pelo token do seu bot
slack_token = 'xoxb...'

# Inicializando o cliente do Slack
client = WebClient(token=slack_token)

try:
    # Troque 'channel-name' pelo nome do canal para o qual você deseja enviar a mensagem
    response = client.chat_postMessage(
      channel='general',
      text="""
      Olá, depois de um vasto período de deliberações com o <@U026X2NB5S5>, o <@U046LTU4TT5> e diversas instâncias de mim mesmo, chegamos a um resultado final. A vencedora da nossa Chuva de Elogios (e bugs :ladybug:) foi:
:drum_with_drumsticks:
:drum_with_drumsticks:
:drum_with_drumsticks:
:drum_with_drumsticks:
:drum_with_drumsticks:

############
#<@U02PSE15QUW>#
############

Parabéns, Laura! :heart:
Aqui vai um texto elogioso que eu fiz pra você baseado nos lindos elogios que o pessoal mandou:

"Parabéns, @Laura Paré! :tada: Arrasou na maratona de elogios e levou o título! Competente, brilhante, e a nova deusa universitária da turma :mortar_board:. Sua energia contagiante faz a diferença todos os dias. Prepare-se para uma chuva de lanches do iFood :hamburger: :pizza:, afinal, quem é a maior merecedora de mimos e lanchinhos se não a aquarianja mais top do pedaço? Aprecie, Laura, este é só o começo da sua jornada brilhante! :star2:"

Aproveita esse voucher do iFood que a <@U02BVD73QRH>, aquela NOIONA, vai mandar pra você :hamburger:.
 """)
    assert response["message"]["text"] == "fala"
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
