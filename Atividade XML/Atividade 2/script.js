const API_KEY = "78e53b49142d1650f21dbf148f366bee"

var dict = {
        "holderNomeCidade": {
          pt_br: "Digite nome da cidade...",
          en: "Enter the city name...",
          fr: "Entrez le nom de la ville...",
          es: "Introduzca el nombre de la ciudad...",
          ja: "都市名を入力してください..."

        },
        "Cidade não encontrada!": {
           pt_br: "Cidade não encontrada!",
           en: "City not found!",
           fr: "Ville introuvable!",
           es: "Ciudad no encontrada!",
           ja: "都市が見つかりません!"
        },
        "tooltipVento": {
            pt_br: "Velocidade do vento",
            en: "Wind speed",
            fr: "Vitesse du vent",
            es: "Velocidad del viento",
            ja: "風速"
        },
        "tooltipTempMin": {
            pt_br: "Temperatura mínima",
            en: "Minimum temperature",
            fr: "Température minimale",
            es: "Temperatura mínima",
            ja: "最低温度"
        },
        "tooltipTempMax" : {
            pt_br: "Temperatura máxima",
            en: "Maximum temperature",
            fr: "Température maximale",
            es: "Temperatura máxima",
            ja: "最高温度"

        },
        "tooltipNascerSol" : {
            pt_br: "Nascer do sol",
            en: "Sunrise",
            fr: "Lever du soleil",
            es: "Amanecer",
            ja: "日の出"
        },
        "tooltipPorSol" : {
            pt_br: "Pôr do sol",
            en: "Sunset",
            fr: "Coucher de soleil",
            es: "Puesta de sol",
            ja: "日没"

        },
        "Configurações" : {
            pt_br: "Configurações",
            en: "Settings",
            fr: "Paramètres",
            es: "Ajustes",
            ja: "設定"
        },
        "Fechar" : {
            pt_br: "Fechar",
            en: "Close",
            fr: "Fermer",
            es: "Cerrar",
            ja: "閉じるには"
        },
        "Salvar" : {
            pt_br: "Salvar",
            en: "Save",
            fr: "Sauver",
            es: "Ahorrar",
            ja: "保存する"

        },
        "Celsius" : {
            pt_br: "Celsius (ºC)",
            en: "Celsius (ºC)",
            fr: "Celsius (ºC)",
            es: "Celsius (ºC)",
            ja: "摂氏 (ºC)"
        },
        "Fahrenheit" : {
            pt_br: "Fahrenheit (ºF)",
            en: "Fahrenheit (ºF)",
            fr: "Fahrenheit (ºF)",
            es: "Fahrenheit (ºF)",
            ja: "華氏 (°F)"
        },
        "Kelvin" : {
            pt_br: "Kelvin (K)",
            en: "Kelvin (K)",
            fr: "Kelvin (K)",
            es: "Kelvin (K)",
            ja: "ケルビン(K)"
        },
        "PortuguêsBR" : {
            pt_br: "Português BR",
            en: "Brazilian Portuguese",
            fr: "Portugais brésilien",
            es: "Portugués brasileño",
            ja: "ブラジルポルトガル語"
        },
        "Inglês" : {
            pt_br: "Inglês",
            en: "English",
            fr: "Anglais",
            es: "Inglés",
            ja: "英語"
        },
        "Francês" : {
            pt_br: "Francês",
            en: "French",
            fr: "Français",
            es: "Francés",
            ja: "フランス語"
        },
        "Espanhol" : {
            pt_br: "Espanhol",
            en: "Spanish",
            fr : "Espagnol",
            es: "Español",
            ja: "スペイン語"
        },
        "Japonês" : {
            pt_br: "Japonês",
            en: "Japanese",
            fr: "Japonais",
            es: "Japonés",
            ja: "日本語"
        }
        
    
}
    
var translator = $('#fundoApp').translate({lang: "pt_br", t: dict}); 
var temperaturaAtual = $("#possiveisTemperaturas")[0].value
var linguaAtual = $("#possiveisLinguas")[0].value
var lingua = "pt_br"
var unidadeMedida = "metric"
var letraTemperatura = obterEscalaTemperatura()
const divInformacoes = document.getElementById("info-clima")

$('#configuracoes').on('click', function(e){
    temperaturaAtual = $("#possiveisTemperaturas")[0].value
    linguaAtual = $("#possiveisLinguas")[0].value
})

$("#fecharConfiguracoes").on('click', function(e){
    $("#possiveisTemperaturas")[0].value = temperaturaAtual
    $("#possiveisLinguas")[0].value = linguaAtual

})

$("#salvarConfiguracoes").on('click', function(e) {
    unidadeMedida = $("#possiveisTemperaturas")[0].value
    lingua = $("#possiveisLinguas")[0].value
    letraTemperatura = obterEscalaTemperatura()
    if(!divInformacoes.classList.contains("invisible")){
        realizarConsulta()
    }
    var cidade = document.getElementById('cidadePesquisar').value
    $('#fundoApp').translate({lang: lingua, t: dict});
    document.getElementById('cidadePesquisar').value = cidade
    
})



function realizarConsulta(){

    const cidadeDigitada = document.getElementById('cidadePesquisar').value
    

    var req = new XMLHttpRequest();
    req.onloadend = function(){
        resp = req.responseText;
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(resp, "text/xml");
        const textoErro = document.getElementById("textoErro")
        
        const cod = xmlDoc.querySelector('cod')

        if(cod == null){
            if(!textoErro.classList.contains("invisible")){
                textoErro.classList.add("invisible")
            }
            if(divInformacoes.classList.contains("invisible")){
                divInformacoes.classList.remove("invisible")
            }


            const valorTemperaturaMin = Math.trunc(xmlDoc.querySelector('temperature').getAttribute('min'))
            const valorTemperatura = Math.trunc(xmlDoc.querySelector('temperature').getAttribute('value'))
            const valorTemperaturaMax = Math.trunc(xmlDoc.querySelector('temperature').getAttribute('max'))
            const horarioNascerSol = new Date(xmlDoc.querySelector('sun').getAttribute('rise')).getTime()
            const horarioPorSol = new Date(xmlDoc.querySelector('sun').getAttribute('set')).getTime()

            const corDeFundo = temperaturaParaCor(obterTemperaturaCelsius(Math.trunc(valorTemperatura)))


            document.getElementById("fundoApp").style.background = 'linear-gradient(to left, ' + corDeFundo + ', white)';

            document.getElementById("temperaturaMin").innerHTML = valorTemperaturaMin + letraTemperatura
            document.getElementById("temperatura").innerHTML = valorTemperatura + letraTemperatura
            document.getElementById("temperaturaMax").innerHTML = valorTemperaturaMax + letraTemperatura
            document.getElementById("descricao").innerHTML = xmlDoc.querySelector('weather').getAttribute('value')
            document.getElementById("velocidadeVento").innerHTML = xmlDoc.querySelector('wind').querySelector('speed').getAttribute('value') + (unidadeMedida === 'imperial' ? ' mph' : ' km/h')
            document.getElementById("cidade").innerHTML = xmlDoc.querySelector('city').getAttribute('name')
            var codigoIcone = xmlDoc.querySelector('weather').getAttribute('icon')
            var icone = "https://openweathermap.org/img/wn/" + codigoIcone + "@4x.png";
            document.getElementById('iconeTempo').setAttribute("src", icone)
            document.getElementById('icone').hidden = false
            document.getElementById('horarioNascerSol').innerHTML = converterUTCparaBrasilia(horarioNascerSol)
            document.getElementById('horarioPorSol').innerHTML = converterUTCparaBrasilia(horarioPorSol)
        }else{
            if(textoErro.classList.contains("invisible")){
                document.getElementById("fundoApp").style.background = 'white'
                divInformacoes.classList.add("invisible")
                textoErro.classList.remove("invisible")
            }
        }
        
    }
    req.open('GET', "https://api.openweathermap.org/data/2.5/weather?q=" + cidadeDigitada + "&appid=" + API_KEY + "&lang=" + lingua + "&units=" + unidadeMedida + "&mode=xml");
    req.send(null);
    
    
}

function obterEscalaTemperatura(){
    if(unidadeMedida === "metric"){
        return "ºC"
    }
    else if(unidadeMedida === "imperial"){
        return "ºF"
    }
    else{
        return "K"
    }
}

function obterTemperaturaCelsius(temperatura){
    if(unidadeMedida === "metric"){
        return temperatura
    }
    else if(unidadeMedida === "imperial"){
        return (temperatura - 32) * 5/9
    }
    else{
        return temperatura - 273
    }
}


function converterUTCparaBrasilia(horarioUTC){

    var data = new Date(horarioUTC * 1000);

    var horas = data.getHours();

    var minutos = data.getMinutes();

    var segundos = data.getSeconds();

    var tempoFormatado = horas.toString().padStart(2,'0') + ":" + minutos.toString().padStart(2,'0') + ":" + segundos.toString().padStart(2, '0')

    return tempoFormatado
}

function temperaturaParaCor(temperatura) {
    if (temperatura < -25){
        return 'rgb(3, 3, 153)'
    }
    else if(temperatura <= -20){
        return 'rgb(0, 7, 196)'
    }
    else if(temperatura <= -15){
        return 'rgb(18, 25, 227)'
    }
    else if(temperatura <= -10){
        return 'rgb(7, 35, 217)'
    }
    else if(temperatura <= 0){
        return 'rgb(4, 55, 207)'
    }
    else if(temperatura <= 5){
        return 'rgb(14, 84, 204)'
    }
    else if(temperatura <= 10){
        return 'rgb(15, 185, 247)'
    }
    else if(temperatura <= 15){
        return 'rgb(49, 174, 212)'
    }
    else if(temperatura <= 20){
        return 'rgb(255, 173, 40)'
    }
    else if(temperatura <= 25){
        return 'rgb(255, 124, 10)'
    }
    else if(temperatura <= 30){
        return 'rgb(255, 75, 10)'
    }
    else if(temperatura <= 35){
        return 'rgb(255, 51, 10)'
    }
    else {
        return 'rgb(255, 10, 10)'
    }
}