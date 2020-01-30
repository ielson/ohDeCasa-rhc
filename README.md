# Ô de casa - RHC

_Para ler esse texto em pt-br, use esse [link](README-PT.md)._

## Introduction
This project aims to be a REST API, that logs and show info about usage of [Raul Hacker Club](https://raulhc.cc/) space.  

#### Prerequisites
The prerequisites  to use this project are: 

A client capable of HTML requisitions, as GET and POST. The recommended service is [cURL](https://curl.haxx.se/) a simple and lightweight command line tool for transfering data to a server, but if you just want to use the GET requisitions a web browser like [firefox](https://www.mozilla.org/pt-BR/firefox/new/) is enough.

Besides that, we'll also need [python](https://www.python.org/) and [flask](https://www.palletsprojects.com/p/flask/) installed. If you need help installing these, the best place are the projects' _installing_ page.
 
 ## How to use
 The first step is to run flask with our project, to do so, go to the clonec repo path and run: 
  `export FLASK_APP=ohDeCasa-api.py` followed by `flask run`
 
 
 #### Status
 To know which members are at RHC in these moment, run the following comand:
 
 `curl localhost:5000/status` 
 
 the result will be a json containing the users at the space and a field called isOpen, showing wheter the place is available for visits or not.
 
 
 #### Check-in 
 If an user arived at the Hacker Club and wants to show others he is there, he just needs to use the _checkin_ endpoint with his user name.
 For the checking-in the user ielson, it's just to run this command:
 
 `curl -H "Content-type: application/json" -d "{\"user\":\"ielson\"}" localhost:5000/checkin`
 
 resulting in checked-in user and check-in time.
 
 #### Check-out
 The check-out function works works reversing what the check-in function does, and it's syntax are the same, you just need to pass the user name to _checkout_ endpoint, like this:
 
 
 `curl -H "Content-type: application/json" -d "{\"user\":\"ielson\"}" localhost:5000/checkout` 
 