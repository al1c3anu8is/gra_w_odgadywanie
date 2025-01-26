def ocena_proby(szyfr, proba):
    """Ocena próby - funkcja, która sprawdza nam ile tych samych liczb jest w szyfrie oraz czy są one na poprawnych miejscach"""
    trafienia = sum(1 for a, b in zip(szyfr, proba) if a == b)  # ilość cyfr, które są na poprawnym miejscu
    wspolne_cyfry = sum(min(szyfr.count(cyfra), proba.count(cyfra)) for cyfra in set(proba))  # Wspólne cyfry, które występują w szyfrie oraz w podanych przez gracza
    nietrafione = wspolne_cyfry - trafienia  # cyfry, które są w naszym szyfrie, ale nie są na poprawnych miejscach
    return trafienia, nietrafione