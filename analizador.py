class AnalizadorTexto:
    def __init__(self, texto: str):
        self._texto = texto

    def contar_lineas(self) -> int:
        return sum(1 for l in self._texto.splitlines() if l.strip())

    def contar_palabras(self) -> int:
        return len(self._texto.split())




