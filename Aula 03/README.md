# Histograma de uma Imagem Digital
 
Um histograma é um gráfico de colunas ou de linhas que representa a <ins>distribuição dos valores dos pixels de uma imagem</ins><br> 
(quantidade de pixeis mais claros próximos de 255 e a quantidade de pixels mais escuros próximos de 0). O eixo X do gráfico<br> 
normalmente possui uma <ins>distribuição de 0 a 255</ins> que demonstra o valor (intensidade) do pixel e no eixo Y é plotada a<br> quantidade de pixels daquela intensidade.
O histograma de uma imagem indica <ins>o número ou o percentual de pixels que a imagem <br>tem em determinado nível de cinza ou cor.</ins>
<br><br><br>
<img src="https://github.com/dep-rookie/processamento-de-img-e-visao-computacional/blob/main/Aula%2003/imagens/ponte_result.jpg" align="center" width="300" height="200"/><img src="https://fabioardito.com/wp-content/uploads/2021/09/img030-800x559-1.jpg" align="center" width="300" height="200"/><img src="https://cdn.cambridgeincolour.com/images/pt/tutorials/hist_examplehist_pt.png" align="center" width="300" height="200"/>
<br><br>
### Equalização do Histograma
+ O histograma fornece uma indicação da qualidade da imagem quanto ao contraste e intensidade luminosa.
+ Equaliza os valores dos pixels de forma que resulte na melhora no contraste da imagem através de um cálculo matemático sobre a
distribuição de pixels.
   - A intenção neste caso é distribuir de forma mais uniforme as intensidades dos pixels sobre a imagem.
<br><br>
### Filtragem de Imagens

As técnicas de filtragem são transformações da imagem pixel a pixel, que não dependem apenas do nível de cinza de um determinado<br>
pixel, mas também do valor dos níveis de cinza dos pixels vizinhos.<br>
O processo de filtragem é feito utilizando matrizes (máscaras), que são aplicadas sobre a imagem com o objetivo corrigir, suavizar ou <br>
realçar determinadas características de uma imagem dentro de uma aplicação específica.
<br><br>
### Suavização de Imagens
A suavização da imagem (Smoothing), também chamada de ‘blur’ ou ‘blurring’, é um efeito que podemos notar nas fotografias desfocadas.<br>
Esse efeito pode ser criado digitalmente, bastando alterar a cor de cada pixel misturando a cor com os pixels ao seu redor.<br>
Esse efeito é muito útil quando utilizamos algoritmos de identificação de objetos em imagens, pois os processos de detecção de bordas<br>
por exemplo, funcionam melhor depois de aplicar uma suavização na imagem.
<br><br>

### Convolução
A convolução é uma operação fundamental no processamento de imagens, onde aplicamos um operador matemático para cada pixel e altera seu valor
de alguma forma. Para aplicar isso operador matemático, usamos outra matriz chamada kernel, que geralmente é muito menor <br>
em tamanho do que a imagem de entrada.

Para cada pixel da imagem, pegamos o kernel e posicionamos no topo de forma que o centro do kernel coincida com o pixel em consideração. Em
seguida, multiplicamos cada valor na matriz do kernel com os valores correspondentes na imagem. Este é o novo valor que será aplicado a esta
posição no imagem de saída. Aqui, o kernel é chamado de filtro de imagem e o processo de aplicação deste kernel na imagem é chamada de
filtragem de imagem. 
A saída obtida após a aplicação do kernel ao imagem é chamada de imagem filtrada e dependendo dos valores do kernel, ele executa funções
diferentes, como desfoque, detecção de bordas e assim por diante.<br><br>
<img src="https://github.com/dep-rookie/processamento-de-img-e-visao-computacional/blob/main/Aula%2003/imagens/Convolucao.png" align="center" width="500" height="200"/>
<br><br>
### Suavização por cálculo da média (BLURRING)
Blurring se refere ao cálculo da média dos valores de pixel em uma vizinhança. Também é chamado de filtro passa-baixo. Uma maneira simples de
construir um filtro passa-baixa é calculando a média uniforme dos valores no vizinhança de um pixel. Podemos escolher o tamanho do kernel 
dependendo de quanto nós deseja suavizar a imagem e, de forma correspondente, terá efeitos diferentes. Se escolhermos um tamanho maior, 
teremos a média de uma área maior. Isso tende a aumentar o efeito de suavização.

Por exemplo, em um kernel de filtro 3x3, dividindo a matriz por 9 porque queremos que os valores sejam um (chamamos de normalização), e é 
importante porque não queremos aumentar artificialmente a intensidade valor na localização desse pixel. Então, um passo importante será 
normalizar o kernel antes de aplicá-lo a um imagem.
<br><br>
### Convolução - Visão Geral
<img src="https://github.com/dep-rookie/processamento-img-e-visao-computacional-aula-03/blob/main/images/Convolucao%20-%20visao%20geral%20(1).png" align="center" width="400" height="200"/>  <img src="https://github.com/dep-rookie/processamento-img-e-visao-computacional-aula-03/blob/main/images/Convolucao%20-%20visao%20geral%20(2).png" align="center" width="500" height="200"/>
<br><br>
