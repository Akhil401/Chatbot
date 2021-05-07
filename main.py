from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

chatbot = ChatBot('Technical Limn')

trainer = ListTrainer(chatbot)


for _file in os.listdir('files'):
    data = open('files/' + _file, 'r').readlines()

    trainer.train(data)

    name = input('May I know your name.?')
    print('Technical_Limn : ', name + ' , Welcome to Technical Limn, How May I assist you.?')


while True:
    request = input('You: ')
    response = chatbot.get_response(request)

    print('Technical_Limn: ', response)
