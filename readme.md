# A Simple Crawler

Um crawler simples e generico para varrer sites e salvar o nome, preço e url dos produtos 

## Getting Started

Run the comand: python main.py

Docker: 

## TODO:
+ Resolver o problema de recursão do python
### Algumas questões


+ Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
Acredito que modificar a aplicação para ser assíncrona seja a solução de escalabilidade, pode ser fazer isso usando uma biblioteca como o asyncio,
o que vou tentar fazer na versão 2 do aplicativo. Nosso app permite instanciar vários sites
+ Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
Usar Selenium seria uma boa solução.
+ Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
time.sleep
+ Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?


### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Just command line: 'python -m pytest'



## Authors

* **Giuliano Lemes** - *website* - [PurpleBooth](http://www.giuice.com)


## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
