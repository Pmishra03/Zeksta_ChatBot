from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

Prbot = ChatBot('Zelo')
from chatterbot import ChatBot


bot = ChatBot(
    'Zelo',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://localhost:27017/chatterbot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm sorry, I didn’t get that.",
          
        },
        'chatterbot.logic.TimeLogicAdapter'
    ]
)
trainer = ListTrainer(bot)

trainer.train([
    'Hii, My name is Zelo...',

    'Hello! Welcome to Zeksta Technology. How can I assist you today?',

    "How are you?",
    "I’m doing great, thank you! How about you?",
    "i am good"
    "oh! great!"

    "What's up?",
    "Not much, just here to help you. What about you?",

    "Nice to meet you",
    "Nice to meet you too! How can I help today?",
    
    'What services do you provide?',
    'We offer web and mobile app development, AI/ML solutions, Chatbot, blockchain, IoT, and digital strategy services, Industry 4.0',
    
    'Do you build chatbots?',
    'Yes! We specialize in developing intelligent chatbots tailored for businesses.',
    
    'Can you help me with mobile app development?',
    'Absolutely! We build scalable, user-friendly mobile applications for both Android and iOS.',
    
    'Where are you located?',
    'We are based in Bengaluru, India and Dallas, USA, serving clients globally.',
    
    'How can I contact you?',
    'You can reach us at solutions@zeksta.com or call us at +91-9620390226 (India) / +1-(214)-473-4395 (USA).',
    
    'What industries do you work with?',
    'We serve clients across healthcare, education, logistics, retail, finance, e-commerce, and more.',
    
    'Thank you',
    'You’re welcome! Is there anything else I can help you with?',
    
    'Bye',
    'Goodbye! Have a great day ahead.'
])


response = 'Hii, My name is Zelo...'

print("Zelo:", response)

name=input("Enter Your Name: ")
print(f"Hi,{name} Welcome to Zeksta Technology")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye' or request == 'stop':
        print('Zelo: Bye')
        print('Thank You, Visit again')
        break
    else:
        response=bot.get_response(request)
        print('Zelo:',response)
