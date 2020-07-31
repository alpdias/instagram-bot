# Python bot for use with Instagram

Python bot to view stories, like and comment on Instagram photos using webdrivers and scranping.

* Script to like: <strong>100%</strong> - Updated (2020/07/29)</br>
* Script to like and comment: <strong>100%</strong> - Updated (2020/07/29)</br>
* Script to see stories: <strong>100%</strong> - Updated (2020/07/29)

Python 3.8.0 </br>
Microsoft VSCode 1.41.1 </br>
Geckodriver v0.26.0 </br>
Coding: -&lowast;- coding: utf-8 -&lowast;- </br>
en-US </br>

![bot-insta](https://github.com/alpdias/bot-python-instagram/blob/master/img/bot-insta.png)

</br>

<strong>Execution:</strong>
 
 * To start and execute the code have the program "geckodriver" on the machine;
 
  https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
  
* Have the latest version of Python 3 installed on the machine;

* Install Python modules;

* Run the command in the terminal:<strong> python bot-instagram.py</strong>;

* Input <strong>'way'</strong> is the path to geckodriver;

* Input <strong>'delay'</strong> is the time in seconds for the pages to load (with good internet use: 2 seconds).

</br>
  
<strong>Python modules</strong>

 > pip install selenium </br>
 > pip install pyfiglet </br>
 
 </br>
 
<strong>Notes:</strong>

* The execution time of the 'comments' function will vary between 6 to 7 minutes, due to the instagram policy on the same functions that are executed repeatedly, the other functions are executed according to the 'delay' entry;

* When executing the function to see 'stories', if the first item is a 'live' it will not be executed and will present an error (working on that part);
 
* The time breaks given within the code will vary according to your internet connection, also observe the instagram policy on likes and comments by hour and day, pay attention to this so that there are no errors and to keep your account without locks;
 
* The buttons within the site to post a comment and deny the notifications described as 'Publish' and 'Not Now' in the code can vary in name according to the language of your instagram, check the DOM for the correct name to run the script;

* The code still does not recognize when the photos are already liked or not, so when going through photos already liked during its execution it will dislike the photo (working on that part).

 ---------------------------------------------------------------------------------------------------------------------

# Bot em Python para usar com o Instagram

Bot em Python para ver stories, curtir e comentar fotos no Instagram, usando webdrivers e scranping.

* Script para curtir: <strong>100%</strong> - Atualizado (29/07/2020)</br>
* Script para curtir e comentar: <strong>100%</strong> - Atualizado (29/07/2020)</br>
* Script para ver stories: <strong>100%</strong> - Atualizado (29/07/2020)

Python 3.8.0 </br>
Microsoft VSCode 1.41.1 </br>
Geckodriver v0.26.0 </br>
Codificação: -&lowast;- coding: utf-8 -&lowast;- </br>
en-US </br>

![bot-insta](https://github.com/alpdias/bot-python-instagram/blob/master/img/bot-insta.png)

</br>

<strong>Execução:</strong>
 
 * Para começar e executar o código tenha o programa "geckodriver" na máquina;
 
  https://github.com/mozilla/geckodriver/releases/tag/v0.26.0
  
* Tenha a última versão do Python 3 instalada na máquina;

* Instale os módulos Python;

* Execute o comando no terminal:<strong> python bot-instagram.py</strong>;

* Entrada <strong>'way'</strong> é o caminho para o geckodriver;

* Entrada <strong>'delay'</strong> é o tempo em segundos para o carregamento das páginas (com uma boa internet use: 2 segundos).

</br>
  
<strong>Módulos Python</strong>

 > pip install selenium </br>
 > pip install pyfiglet </br>
 
 </br>
 
<strong>Observações:</strong>

* O tempo de execução da função de 'comentários' vai variar entre 6 a 7 minutos, devido a política do instagram sobre mesmas funções que são executadas repetitivamente, as demais funções são executadas de acordo com a entrada 'delay';

* Ao executar a função para ver 'stories', caso o primeiro item seja uma 'live' ele não vai ser executado e apresentará um erro (trabalhando nessa parte);
 
* As pausas de tempo dadas dentro do código vão variar de acordo com sua conexão de internet, observe também a política do instagram sobre curtidas e comentários por hora e dia, atente-se a isso para que não ocorra erros e para manter sua conta sem bloqueios;
 
* Os botões dentro do site para publicar um comentário e negar as notificações descritos respectivamente como 'Publicar' e 'Agora não' no código podem variar de nome de acordo com o idioma do seu instagram, verifique no DOM o nome correto para executar o script;

* O código ainda não reconhece quando as fotos já estão curtidas ou não, então ao passar por fotos já curtidas durante sua execução ele ira descurtir a foto (trabalhando nessa parte).
 
----------------------------------------------------------------------------------------------------------------------
