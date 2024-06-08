from flask import Flask, render_template
from quizzes.quiz import quizzes_by_topic

# Cria uma instância da aplicação Flask
app = Flask(__name__)

class Quiz:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions

    def to_dict(self):
        return {
            'topic': self.topic,
            'questions': [question.to_dict() for question in self.questions]
        }

class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def to_dict(self):
        return {
            'text': self.text,
            'options': self.options
        }

# Define uma rota para a página inicial
@app.route('/')
def index():
    # Convertendo os objetos Quiz em dicionários antes de passá-los para o template
    quizzes_serializable = {topic: quiz.to_dict() for topic, quiz in quizzes_by_topic.items()}
    return render_template('index.html', quizzes_by_topic=quizzes_serializable)

# Verifica se o arquivo main.py está sendo executado diretamente e, se sim, inicia o servidor Flask
if __name__ == "__main__":
    # Ativa o modo de depuração para facilitar o desenvolvimento
    app.run(debug=True)
