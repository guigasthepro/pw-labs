const darkModeBtn = document.getElementById("dark-mode-btn");
const body = document.body;

darkModeBtn.addEventListener("click", () => {
  body.classList.toggle("dark-mode");
});

function calcular() {
    let expressao = document.getElementById("expressao").value;
    let resultado = eval(expressao);
    document.getElementById("resultado").innerText = resultado;
  }
  
  function apagar() {
    document.getElementById("expressao").value = "";
    document.getElementById("resultado").innerText = "";
  }

const fraseInspiradora = document.getElementById('frase-inspiradora');
const imagem = document.querySelector('img');

fraseInspiradora.addEventListener('input', () => {
imagem.setAttribute('title', fraseInspiradora.value);
});

const dataAtual = new Date();
const dataAtualElemento = document.getElementById('data-atual');
const options = { day: 'numeric', month: 'long', year: 'numeric' };

dataAtualElemento.innerText = dataAtual.toLocaleDateString('pt-PT', options);