# OPE | Daniel Gomes Molina
Oficina Projeto Empresa IMPACTA - 2020

Acesse a plataforma desenvolvida em https://so-manager.herokuapp.com/

# Arquitetura da Solução

A visão de cenários do sistema foi descrita através do diagrama de casos de uso demonstrado na Figura 1. Nele, estão representados os principais requisitos funcionais que compõem a solução.

![image](https://user-images.githubusercontent.com/60905534/113339980-ad7f8d00-9301-11eb-8d75-7ffb6004c1c9.png)<br>
**Figura 1. Diagrama de Casos de Uso.**

**Diagrama de Componentes**<br>
A estrutura do software foi dividida em dois módulos. Um módulo é responsável por toda lógica referente ao gerenciamento das informações do cliente, enquanto o outro é reponsável pela lógica referente ao gerenciamento das ordens de serviço.

O diagrama de componentes demonstrado na Figura 2, foi utilizado para representar a visão de desenvolvimento do sistema.

![image](https://user-images.githubusercontent.com/60905534/113340383-35659700-9302-11eb-96cc-411f45abafa0.png)<br>
**Figura 2. Diagrama de Componentes.**

A divisão entre módulos permite o desenvolvimento de componentes especializados, facilitando o desenvolvimento de novas funcionalidades, e permitindo que o sistema seja expandido gradualmente.

**Infraestrutura**<br>
A infraestrutura necessária para disponibilizar o software será composta por um servidor de aplicação, implementado dentro de um container mantido pela plataforma de cloud, Heroku. A plataforma possui um sistema de dynos, que fornece containers leves, ideais para aplicações de pequeno porte.

Para representar a visão física do sistema, foi utilizado o diagrama de implantação demonstrado na Figura 3.

![image](https://user-images.githubusercontent.com/60905534/113340629-86758b00-9302-11eb-8f3a-4c07e002ddab.png)<br>
**Figura 3. Diagrama de Implantação.**

**Tecnologias Utilizadas**<br>
A seguir, segue a tabela com as principais tecnologias utilizadas no sistema.

Tecnologia | Camada/Subsistema | Justificativa
---------- | ----------------- | -------------
Git | Infraestrutura | Versionamento de código distribuído entre todos os desenvolvedores. <br><br>Facilita o trabalho em equipe e o acompanhamento do desenvolvimento por todos os membros da equipe.
Heroku | Infraestrutura | É uma plataforma em nuvem que permite o deploy de aplicações back-end escaláveis.<br><br>É utilizada, tanto para o ambiente de testes, quanto para o ambiente de produção.
Flask | Servidor/Cliente | Framework web, leve, que permite a criação de aplicações de pequeno porte eficientes e seguras.<br><br>É responsável pelo back-end e front-end da aplicação.
Bootstrap | Cliente | Biblioteca de componentes front-end amplamente aceita pelo mercado de aplicações.<br><br>Facilita o desenvolvimento, e diminui o tempo de produção das interfaces.
Python | Servidor | Linguagem de programação utilizada pelo framework Flask, e de maior familiaridade do autor do projeto.
PostgreSQL | Servidor | SGBD Relacional de licença gratuita. Escolhido pela familiaridade do autor com o modelo relacional.
