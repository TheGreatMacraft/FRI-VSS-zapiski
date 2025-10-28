class Ladja:
    def __init__(self):
        strani = [0,0]
        stran_nalaganja = False

    def nalozi(cls, teza):
        if(abs(cls.strani[cls.stran_nalaganja] + teza - cls.strani[not cls.stran_nalaganja]) <= 10):
            cls.strani[cls.stran_nalaganja] += teza
            cls.stran_nalaganja = not cls.stran_nalaganja
            return True
        return False

    def obremenitev(cls):
        return cls.strani[0] + cls.strani[1]
