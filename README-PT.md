# Ô de casa - RHC
_To read this in english, please use this [link](README.md)._

## Introdução
Esse projeto tem como objetivo criar uma REST API que possa ser usada para saber se tem alguém no [Raul Hacker Club](https://raulhc.cc/), bem como outras informações sobre a utilização do espaço.

Para utilização é necessário um cliente capaz de fazer requisições HTML, mais especificamente GET e POST. Para os serviços que usem GET, um browser (como o [firefox](https://www.mozilla.org/pt-BR/firefox/new/)) é suficiente, já para os POSTs, eu recomendo um serviço como o [cURL](https://curl.haxx.se/). 

Além disso é preciso do [flask](https://www.palletsprojects.com/p/flask/) instalado, para instruções de instalação, verificar na página principal do projeto.
 
 ## Modo de utilização
 O primeiro passo é rodar o flask com nosso arquivo, para isso basta ir na pasta em que se encontra o clone do repositório, e usar o seguinte comando 
 `export FLASK_APP=ohDeCasa-api.py` e então o comando `flask run`.
 
 Para ilustrar a utilização da API vamos usar o cURL a partir de agora.
 
 #### Status de Ocupação
 Para saber se o espaço está ocupado ou não e quais membros estão lá neste momento, abra o terminal e digite o seguinte comando:
 
 `curl localhost:5000/status` 
 
 e o resultado será um json com os usuários no espaço neste momento bem como o campo isOpen que indica se o RHC está aberto ou não.
 
 #### Check-in 
 Se um usuário chegou no espaço e deseja mostrar aos outros membros que ele está lá, é só usar o endpoint checkin
 com o cURL contendo seu nome de usuário, para um usuário chamado ielson, teremos o seguinte comando:
 
 `curl -H "Content-type: application/json" -d "{\"user\":\"ielson\"}" localhost:5000/checkin`
 
 qeu traz como resultado o nome do usuário com a hora em que ele fez login.
 
 #### Check-out
 No momento que o usuário faz sair do espaço, ele pode fazer check-out na api usando o seguinte comando
 
 `curl -H "Content-type: application/json" -d "{\"user\":\"ielson\"}" localhost:5000/checkout` 
 