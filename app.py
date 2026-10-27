def executar_brainfuck(codigo):
    comandos_validos = set('><+-.,[]')
    codigo = ''.join(c for c in codigo if c in comandos_validos)

    fita = [0] * 30000
    ptr = 0
    i = 0
    pilha = []
    mapa = {}

    # Mapeia colchetes
    for pos, cmd in enumerate(codigo):
        if cmd == '[':
            pilha.append(pos)
        elif cmd == ']' and pilha:
            inicio = pilha.pop()
            mapa[inicio] = pos
            mapa[pos] = inicio

    saida = []
    while i < len(codigo):
        cmd = codigo[i]
        if cmd == '>': 
            ptr = min(29999, ptr + 1)
        elif cmd == '<': 
            ptr = max(0, ptr - 1)
        elif cmd == '+': 
            fita[ptr] = (fita[ptr] + 1) % 256
        elif cmd == '-': 
            fita[ptr] = (fita[ptr] - 1) % 256
        elif cmd == '.': 
            saida.append(fita[ptr])
        elif cmd == ',': 
            fita[ptr] = ord(input('\nEntrada: ')[0])
        elif cmd == '[' and fita[ptr] == 0: 
            i = mapa[i]
        elif cmd == ']' and fita[ptr] != 0: 
            i = mapa[i]
        i += 1

    # Imprime de forma segura — resolve problema do Windows
    import sys
    sys.stdout.buffer.write(bytes(saida))
    sys.stdout.buffer.flush()


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as arq:
                codigo = arq.read()
            executar_brainfuck(codigo)
            print("\n✅ Execução concluída!")
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {sys.argv[1]}")
    else:
        print("ℹ️ Uso: python app.py 03-imprimir-com-loop.bf")