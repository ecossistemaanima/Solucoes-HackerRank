<img width="641" alt="Captura de tela 2024-08-05 150625" src="https://github.com/user-attachments/assets/8550873d-931b-4495-bf39-d796d803dc7a">

Tanto o ponteiro da esquerda quanto da direita avançam em direção ao centro. Dado a string "aaab":

- Á medida que os ponteiros avançam, é checado se s[l+1:r+1] é um palindromo: "aab". Caso seja seja, o char a ser retirado é o primeiro "a".

- É checado se s[l+1:r+1] é um palindromo: "aaa". Caso seja, o char a ser retirado é o último "b".
