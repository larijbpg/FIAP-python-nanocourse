# Desenvolvimento de um aplicativo "Wazeyes"

## Contexto:
### Um grupo de pesquisa, patrocinado pela BitMed, voltado para o desenvolvimento de "wearables" aplicados ao setor da saúde, está desenvolvendo um aplicativo, denominado "Wazeyes", que irá trocar coordenadas geográficas com um wearable a fim de orientar pessoas com necessidades especiais visuais. O paciente irá digitar o endereço e o aplicativo deverá converte-lo em coordenadas geográficas(latitude e longitude), para que possa marcar a posição no mapa (GoogleMaps ouOpenStreepMap) e assim, orientar, por voz, o deslocamento da pessoa portadora de necessidade especial visual.

## Função: 
### desenvolver o código(ficará no servidor) que será responsável por capturar o endereço que estará dentro de um arquivo JSON(gerado pelo app instalado no dispositivo mobile do portador de necessidade especial visual) e, então, passar as coordenada para outro arquivo JSON que será consumido por outra aplicação que manipula mapas e desenvolve rotas. 

## Arquitetura:
* ETAPA 1: No app movel
- receber o endereço, por voz ou texto, e gerar um arquivo JSON no servidor, com o endereço que foi digitado/falado

* ETAPA 2: APLICAÇÃO PYTHON
- realizar a leitura do arquivo JSON(entrada.son), que armazena o endereço e, então, deverá escrever um outro arquivo JSON(saida.json) as coordenadas geográficas referentes ao endereço

* ETAPA 3: 
- outra aplicação irá consumir o arquivo "sainda.json", dentro de determinado intervalo de tempo e, então, irá gerar uma rota que será exibida ao portador da necessidade especial visual, somente quando ele ativar o botão "iniciar o trajeto"

