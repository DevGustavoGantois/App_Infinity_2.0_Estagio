/*
        DOCUMENTAÇÃO DO CÓDIGO JAVASCRIPT PARA O CONSUMO DA API DO GOOGLE MAPS

CABEÇALHO:
---------------------------------------------------------------------
ARQUIVO: js/scripts.js
---------------------------------------------------------------------
AUTOR DO CÓDIGO: GUSTAVO GANTOIS CARIA CARVALHO
---------------------------------------------------------------------
DATA DA REALIZAÇÃO DO CÓDIGO: 20/05/2024 
----------------------------------------------------------------------
DEPENDÊNCIAS: 
-Javascript Vaniila
-Consumo de API Google Places API
-AJAX
-JSON
----------------------------------------------------------------------
FUNÇÕES: 

function calcularRota() => Está função serve para pegar os inputs do formulário pelos IDS
dos mesmos, apos isso utiliza o new google maps direction service para utilizar o serviço do google maps
e o renderer para renderizar esse serviço na nossa aplicação
let map iniciará o mapa do google maps co a latitude e longitude do centro do brasil, apos isso
damos um set map para gerenciar o estado deste mapa, com let request configuramos a solicitação para serviços de
direções com o valor de origem, destino, e tipo de viagem
enviamos a solicitação para calcular a rota, apos isso faremos uma verificação se a solicitação foi bem sucedida
ela renderiza a rota do mapa obtendo informações sobre a rota mostrando.
Atualizamos o HTML com as informações da rota através dos Ids depois do innerText e depois mostramos a route.distance , route.duration
Mostramos uma frase através do Id e depois envia os dados da rota para o flask após calcular com sucesso
utilizando o JSON.stringify e exibindo um alerta que não foi possivel calcular a rota, caso o bloco anterior não funcione.
Depois utilizamos o autocompletar para o campo de origem e destino usando a API, mostrando o tipo que será geocode e 
o continente br (BRASIL).
--------------------------------------------------------------------------------------------------------------------------------------------

DESCRIÇÃO: Esse script consome a API do Google Places API para mostrar rotas de acordo com o input do usuário mostrando a distância, CEP, 
Localização tempo de um veículo até chegar ao determinado local desejado pelo usuário logado na conta.

--------------------------------------------------------------------------------------------------------------------------------------------
VERSÃO: 2.0
*/ 


//Fazendo o script para calcular a distâncio
// Define a função para calcular a rota

let intervalId; // Define a variável para controlar o intervalo

document.getElementById('rotaForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário

    // Limpa os valores anteriores ao calcular a nova rota
    limparValores();

    // Obtém os elementos de origem e destino do formulário
    let origem = document.getElementById('origem').value;
    let destino = document.getElementById('destino').value;

    // Inicializa o serviço de direções e o renderizador de direções do Google Maps
    let directionsService = new google.maps.DirectionsService();
    let directionsRenderer = new google.maps.DirectionsRenderer();

    // Inicializa o mapa do Google Maps
    let map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: { lat: -15.7942, lng: -47.8822 } // Centro do Brasil
    });

    // Define o mapa a ser usado pelo renderizador de direções
    directionsRenderer.setMap(map);

    // Configura a solicitação para o serviço de direções
    let request = {
        origin: origem,
        destination: destino,
        travelMode: google.maps.TravelMode.DRIVING
    };

    // Envia a solicitação para calcular a rota
    directionsService.route(request, function(response, status) {
        if (status === google.maps.DirectionsStatus.OK) {
            // Renderiza a rota no mapa
            directionsRenderer.setDirections(response);

            // Obtém informações sobre a rota
            let route = response.routes[0].legs[0];

            // Converte a distância para metros e a duração para segundos
            let distanciaMetros = route.distance.value;
            let duracaoSegundos = route.duration.value;

            // Limpa o intervalo anterior, se existir
            if (intervalId) {
                clearInterval(intervalId);
            }

            // Função para atualizar a distância e a duração
            function atualizarDistanciaDuracao() {
                if (distanciaMetros > 0 && duracaoSegundos > 0) {
                    distanciaMetros -= 100; // Diminui 100 metros por intervalo
                    duracaoSegundos -= 10; // Diminui 10 segundos por intervalo

                    // Converte metros de volta para quilômetros
                    let distanciaKm = (distanciaMetros / 1000).toFixed(2);
                    // Converte segundos de volta para horas e minutos
                    let horas = Math.floor(duracaoSegundos / 3600);
                    let minutos = Math.floor((duracaoSegundos % 3600) / 60);
                    let duracaoTexto = `${horas}h ${minutos}m`;

                    // Atualiza o HTML com os novos valores
                    document.getElementById('distancia').innerText = `${distanciaKm} km`;
                    document.getElementById('duracao').innerText = duracaoTexto;
                    document.getElementById('endereco_origem').innerText = route.start_address;
                    document.getElementById('endereco_destino').innerText = route.end_address;

                    // Constrói e exibe uma frase com informações sobre a rota
                    let frase = `O tempo estimado de ${route.start_address} para ${route.end_address} de carro é de ${duracaoTexto}`;
                    document.getElementById('frase').innerText = frase;
                } else {
                    clearInterval(intervalId); // Para a contagem regressiva quando chegar a zero
                }
            }

            // Atualiza os valores a cada segundo (1000 ms)
            intervalId = setInterval(atualizarDistanciaDuracao, 1000);

            // Envia os dados da rota para o Flask após calcular com sucesso
            fetch('/app', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    origem: origem,
                    destino: destino,
                    distancia: route.distance.text,
                    duracao: route.duration.text,
                    endereco_origem: route.start_address,
                    endereco_destino: route.end_address
                })
            })
            .then(response => response.json())
            .then(data => {
                // Atualiza o DOM com a resposta do backend, se necessário
                console.log('Resposta do backend:', data);
            })
            .catch(error => {
                console.error('Erro ao enviar dados para o Flask:', error);
            });
        } else {
            alert('Não foi possível calcular a rota: ' + status);
        }
    });
});

// Função para limpar os valores anteriores ao calcular uma nova rota
function limparValores() {
    document.getElementById('distancia').innerText = '';
    document.getElementById('duracao').innerText = '';
    document.getElementById('endereco_origem').innerText = '';
    document.getElementById('endereco_destino').innerText = '';
    document.getElementById('frase').innerText = '';
    
    // Limpa o intervalo de atualização de distância e duração, se existir
    if (intervalId) {
        clearInterval(intervalId);
    }
}

// Inicializa o autocompletar para o campo de origem usando a API de Places do Google Maps
let autocompleteOrigem = new google.maps.places.Autocomplete(document.getElementById('origem'), {
    types: ['geocode'],
    componentRestrictions: { country: 'br' }
});

// Inicializa o autocompletar para o campo de destino usando a API de Places do Google Maps
let autocompleteDestino = new google.maps.places.Autocomplete(document.getElementById('destino'), {
    types: ['geocode'],
    componentRestrictions: { country: 'br' }
});


