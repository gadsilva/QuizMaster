# Lógica relacionada aos quizzes
# QuizMaster/quizzes/quiz.py

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        self.questions.remove(question)

# Dicionário contendo os quizzes por tópico
quizzes_by_topic = {
    "Introdução à Programação": Quiz(
        "Introdução à Programação",
        [
            Question("O que é um algoritmo?", ["A. Um tipo de programa", "B. Um tipo de linguagem de programação", "C. Um conjunto de instruções passo a passo para resolver um problema", "D. Uma estrutura de dados"], "C"),
            Question("Qual é a linguagem de programação mais popular para iniciantes?", ["A. Python", "B. Java", "C. C++", "D. JavaScript"], "A"),
        ]
    ),
    "Lógica de Programação": Quiz(
        "Lógica de Programação",
        [
            Question("O que é uma condição 'if'?", ["A. Uma estrutura de repetição", "B. Uma função", "C. Um operador lógico", "D. Um comando de decisão"], "D"),
            Question("Qual é o resultado de 5 + 3 * 2?", ["A. 16", "B. 11", "C. 10", "D. 13"], "D"),
        ]
    ),
    "Introdução a Estruturas de Dados": Quiz(
        "Introdução a Estruturas de Dados",
        [
            Question("O que é uma lista encadeada?", ["A. Uma estrutura de dados que contém uma coleção de elementos", "B. Uma sequência de elementos de dados, onde cada elemento se conecta ao próximo elemento", "C. Uma estrutura de dados que armazena dados em pares chave-valor", "D. Uma estrutura de dados que permite acesso aleatório aos elementos"], "B"),
        ]
    ),
    "Fundamentos de Hardware e Software": Quiz(
        "Fundamentos de Hardware e Software",
        [
            Question("O que é um processador?", ["A. Um dispositivo de entrada", "B. Um dispositivo de saída", "C. Uma unidade de processamento central que executa instruções armazenadas", "D. Um dispositivo de armazenamento de dados"], "C"),
        ]
    ),
    "Noções de Bancos de Dados": Quiz(
        "Noções de Bancos de Dados",
        [
            Question("O que é um banco de dados relacional?", ["A. Um tipo de banco de dados que armazena dados de forma hierárquica", "B. Um banco de dados que utiliza linguagem de consulta estruturada (SQL)", "C. Um banco de dados que não permite a criação de relacionamentos entre tabelas", "D. Um banco de dados que armazena dados em formato de documentos"], "B"),
        ]
    ),
    "Redes de Computadores": Quiz(
        "Redes de Computadores",
        [
            Question("O que é um endereço IP?", ["A. Um identificador único atribuído a cada dispositivo em uma rede", "B. Uma unidade de medida de velocidade de internet", "C. Um protocolo de comunicação usado para transferir arquivos", "D. Um software usado para acessar a internet"], "A"),
        ]
    ),
    "Introdução à Web": Quiz(
        "Introdução à Web",
        [
            Question("O que é HTML?", ["A. Uma linguagem de programação", "B. Um sistema operacional", "C. Uma linguagem de marcação usada para criar páginas da web", "D. Um software de design gráfico"], "C"),
        ]
    ),
    "Algoritmos Básicos": Quiz(
        "Algoritmos Básicos",
        [
            Question("O que é um algoritmo de ordenação?", ["A. Um algoritmo usado para encontrar a posição de um elemento em uma lista", "B. Um algoritmo usado para reorganizar os elementos de uma lista em uma ordem específica", "C. Um algoritmo usado para encontrar o maior elemento em uma lista", "D. Um algoritmo usado para remover elementos duplicados de uma lista"], "B"),
        ]
    ),
    "Introdução à Engenharia de Software": Quiz(
        "Introdução à Engenharia de Software",
        [
            Question("O que é o modelo de desenvolvimento de software 'cascata'?", ["A. Um modelo de desenvolvimento ágil", "B. Um modelo de desenvolvimento incremental", "C. Um modelo de desenvolvimento sequencial, onde cada fase deve ser concluída antes da próxima começar", "D. Um modelo de desenvolvimento baseado em prototipagem"], "C"),
        ]
    ),
    "Desenvolvimento de Software Básico": Quiz(
        "Desenvolvimento de Software Básico",
        [
            Question("O que é um IDE?", ["A. Um ambiente de desenvolvimento integrado", "B. Um tipo de linguagem de programação", "C. Um sistema operacional", "D. Um dispositivo de entrada"], "A"),
        ]
    ),
    # Adicionar mais tópicos e quizzes conforme necessário
}

# Função para obter um quiz por tópico
def get_quiz_by_topic(topic):
    return quizzes_by_topic.get(topic)
