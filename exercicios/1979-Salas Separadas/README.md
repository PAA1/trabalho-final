# Problema Exemplo: Nome do Problema

**Problema:** [Nome do Problema](link_para_o_problema)  

---

## 📌 Descrição do Problema

> O problema consiste em verificar se é possível dividir os estudantes em duas salas, de modo que nenhum par de amigos fique na mesma sala.

---

## 💡 Abordagem

> Percebi que podíamos transformar cada estudante em um nodo, e suas relações de amizade em arestas, assim tentado separar o grafo em 2 grupos, de modo que nenhuma aresta toque dois nodos do mesmo grupo. Isso é um teste de bipartição.

---

## ❌ O Que Não Funcionou

> Minha maior dificuldade foi em conseguir debugar o código para passar nos exemplos do beecrowd, mas percebi que o código do beecrowd que está errado, pois ele checa apenas o componente conexo a partir do estudante de id 1, ou seja se houver outro componente conexo não bipartido, ele ignora. Então alterei meu código para passar no beecrowd, mas o algoritmo que commitei é o correto que não passa 100% no beecrowd.

---

## 📊 Análise de Complexidade

### Tempo

O(V + E) por se tratar de uma construção de grafo e verificação de bipartição


### Espaço

> O(V + E) também, considerando grafo, deque e dicionário de cores

## 🔍 Corretude

> A corretude do algoritmo é garantida pela utilização da BFS, que atribui cores alternadas aos vértices adjacentes. Caso dois estudantes amigos recebam a mesma cor, o algoritmo identifica que o grafo não é bipartido e retorna "NAO". Caso contrário, retorna "SIM", indicando que foi possível dividir os estudantes em dois grupos sem que amigos pertençam ao mesmo grupo.

---

## 🚀 O Que Poderia ser Melhorado

> O algoritmo apresenta boa eficiência, com complexidade de tempo O(V + E) e espaço O(V + E). A utilização da BFS é adequada para verificar se o grafo é bipartido, percorrendo todos os seus componentes. Embora não exista uma melhoria significativa na complexidade, o código poderia ser aprimorado em legibilidade e organização, além de considerar possíveis entradas inválidas ou incompletas.


---

## 📸 Evidência de Submissão

> ![alt text](image.png)
