from pathlib import Path

caminho = Path('records')
caminho.mkdir(exist_ok=True)

(caminho / 'pontuacao.txt').write_text('Jogador1: 2500 pontos')
