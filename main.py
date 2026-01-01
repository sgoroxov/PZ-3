ABC_EN = 'abcdefghijklmnopqrstuvwxyz'
ABC_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def _shift_char(ch: str, k: int) -> str:
    """Вспомогательная функция для посимвольного сдвига."""
    low = ch.lower()

    for alphabet in (ABC_EN, ABC_RU):
        if low in alphabet:
            pos = alphabet.index(low)
            new = alphabet[(pos + k) % len(alphabet)]
            return new.upper() if ch.isupper() else new

    return ch


def caesar(text: str, step: int) -> str:
    return ''.join(_shift_char(c, step) for c in text)


def atbash(text: str) -> str:
    result = []
    for ch in text:
        low = ch.lower()
        if low in ABC_EN:
            idx = ABC_EN.index(low)
            m = ABC_EN[-idx - 1]
            result.append(m.upper() if ch.isupper() else m)
        else:
            result.append(ch)
    return ''.join(result)


class CipherField:
    """Дескриптор, возвращающий зашифрованное значение при чтении."""

    def __init__(self, mode='caesar', step=3):
        self.mode = mode
        self.step = step
        self._plain = ''

    def __get__(self, obj, objtype=None):
        return (
            caesar(self._plain, self.step)
            if self.mode == 'caesar'
            else atbash(self._plain)
        )

    def __set__(self, obj, value):
        self._plain = value


class Demo:
    text_c = CipherField('caesar', 3)
    text_a = CipherField('atbash')


# --- верхнеуровневое выполнение (без __main__ и функций) ---

demo = Demo()

demo.text_c = 'Привет, мир!'
print('Цезарь:', demo.text_c)
print('Дешифровка:', caesar(demo.text_c, -3))

demo.text_a = 'Hello, World!'
print('Атбаш:', demo.text_a)
print('Дешифровка:', atbash(demo.text_a))
