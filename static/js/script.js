// Simulação de dados do quiz para testes
const quizData = {
  "Introdução à Programação": {
      "questions": [
          {
              "text": "O que é uma variável?",
              "options": ["Um valor constante", "Um valor que pode mudar", "Um tipo de dado", "Uma função"],
              "correct_answer": "Um valor que pode mudar"
          },
          {
              "text": "Qual a função principal de um loop?",
              "options": ["Repetir uma série de instruções", "Parar o código", "Definir variáveis", "Declarar funções"],
              "correct_answer": "Repetir uma série de instruções"
          }
      ]
  },
  "Lógica de Programação": {
      "questions": [
          {
              "text": "O que é um algoritmo?",
              "options": ["Uma linguagem de programação", "Uma sequência de instruções", "Um tipo de dado", "Um erro no código"],
              "correct_answer": "Uma sequência de instruções"
          },
          {
              "text": "Qual é o objetivo de usar uma estrutura condicional?",
              "options": ["Repetir código", "Tomar decisões com base em condições", "Declarar variáveis", "Organizar funções"],
              "correct_answer": "Tomar decisões com base em condições"
          }
      ]
  }
};

// Função para iniciar o quiz com o tópico selecionado
function startQuiz(topic) {
  currentTopicIndex = Object.keys(quizData).indexOf(topic);
  document.getElementById('startQuizButton').style.display = 'none';
  document.getElementById('quizQuestions').style.display = 'block';
  showQuestion();
}        

// Variáveis para controlar a navegação pelo quiz
let currentTopicIndex = 0;
let currentQuestionIndex = 0;
let userAnswers = {};

// Função para mostrar a próxima pergunta
function showQuestion() {
  const topic = Object.keys(quizData)[currentTopicIndex];
  const questions = quizData[topic].questions;
  const question = questions[currentQuestionIndex];
  const questionsList = document.getElementById('questionsList');
  questionsList.innerHTML = '';

  // Adiciona a pergunta ao HTML com a classe de animação
  const questionItem = document.createElement('li');
  questionItem.className = 'animated-question-item';
  questionItem.innerHTML = `
      <h4>${question.text}</h4>
      ${question.options.map((option, index) => `
          <input type="radio" id="option-${index}" name="answer" value="${option}">
          <label for="option-${index}">${option}</label><br>
      `).join('')}
  `;
  questionsList.appendChild(questionItem);
}

// Função para lidar com o envio das respostas
function submitAnswers() {
  const selectedAnswer = document.querySelector('input[name="answer"]:checked');
  if (selectedAnswer) {
      userAnswers[currentQuestionIndex] = selectedAnswer.value;
      currentQuestionIndex++;
      const topic = Object.keys(quizData)[currentTopicIndex];
      const questions = quizData[topic].questions;
      if (currentQuestionIndex < questions.length) {
          showQuestion();
      } else {
          currentTopicIndex++;
          currentQuestionIndex = 0;
          if (currentTopicIndex < Object.keys(quizData).length) {
              showQuestion();
          } else {
              showResults();
          }
      }
  } else {
      alert('Por favor, selecione uma resposta.');
  }
}

// Função para mostrar os resultados do quiz
function showResults() {
  document.getElementById('quizQuestions').style.display = 'none';
  document.getElementById('quizResults').style.display = 'block';

  let correctAnswers = 0;
  let incorrectAnswers = 0;
  let incorrectQuestionsHTML = '';

  for (let i = 0; i < Object.keys(quizData).length; i++) {
      const topic = Object.keys(quizData)[i];
      const questions = quizData[topic].questions;
      for (let j = 0; j < questions.length; j++) {
          const correctAnswer = questions[j].correct_answer;
          const userAnswer = userAnswers[j];
          if (userAnswer === correctAnswer) {
              correctAnswers++;
          } else {
              incorrectAnswers++;
              // Adiciona a questão incorreta ao HTML
              incorrectQuestionsHTML += `<p>${questions[j].text} - Resposta correta: ${correctAnswer}</p>`;
          }
      }
  }

  const scoreElement = document.getElementById('score');
  scoreElement.textContent = `Sua pontuação: ${correctAnswers} de ${correctAnswers + incorrectAnswers}`;

  const correctAnswersElement = document.getElementById('correctAnswers');
  correctAnswersElement.textContent = `Respostas corretas: ${correctAnswers}`;

  const incorrectAnswersElement = document.getElementById('incorrectAnswers');
  incorrectAnswersElement.textContent = `Respostas incorretas: ${incorrectAnswers}`;

  const incorrectQuestionsElement = document.getElementById('incorrectQuestions');
  incorrectQuestionsElement.innerHTML = `<h3>Questões respondidas incorretamente:</h3>${incorrectQuestionsHTML}`;
}

// Adiciona um evento de clique ao botão "Começar Quiz"
document.getElementById('startQuizButton').addEventListener('click', () => {
  document.getElementById('startQuizButton').style.display = 'none';
  document.getElementById('topicIcons').style.display = 'block';
  animateIcons();
});

// Adiciona um evento de clique ao botão "Enviar Respostas"
document.getElementById('submitButton').addEventListener('click', submitAnswers);

// Função para adicionar a classe de animação aos ícones
function animateIcons() {
  const icons = document.querySelectorAll('.topic-icon');
  icons.forEach(icon => {
      icon.classList.add('animated');
  });
}
