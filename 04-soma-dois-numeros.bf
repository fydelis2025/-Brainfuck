+++++     ; Célula 0 = 5
>+++      ; Célula 1 = 3
[<+>-]    ; Move Célula 1 para a Célula 0 (Célula 0 agora vale 8, Célula 1 vale 0)
>         ; Vai para a Célula 1
++++++++++++++++++++++++++++++++++++++++++++++++ ; Célula 1 = 48 (código ASCII para '0')
[<+>-]    ; Soma 48 da Célula 1 para a Célula 0 (Célula 0 vira 56, que é o caractere '8')
<.        ; Volta para a Célula 0 e imprime o caractere '8'