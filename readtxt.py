from random import choice


def filer() -> list[str]:
    """Возвращает список всех фактов о COVID-19"""
    with open(r"Inf.txt", "r", encoding='utf-8') as fin:
        result = fin.read().split('\n')
    return result


def arbitrary() -> str:
    """Возвращает рандомный факт"""
    return choice(filer())
