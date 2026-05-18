from pathlib import Path

caminho = Path('mochila')
caminho.mkdir(exist_ok=True)

(caminho / 'itens.txt').write_text('Espada de Ferro, Poção de Vida, Escudo')
