KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        tarkistaja = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lista[i]:
                tarkistaja = tarkistaja + 1
        if tarkistaja > 0:
            return True
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lista[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        if not self.kuuluu(n):
            self.lisaa2(n)
            return True
        return False

    def lisaa2(self, n):
        self.lista[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1
        if self.alkioiden_lkm % len(self.lista) == 0:
            taulukko_old = self.lista
            self.kopioi_lista(self.lista, taulukko_old)
            self.lista = self._luo_lista(
                self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.lista)
        return True

    def poista(self, n):
        kohta = -1
        apumuuttuja = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.lista[i]:
                kohta = i
                self.lista[kohta] = 0
                break
        if kohta != -1:
            self.poista2(kohta, apumuuttuja)
            return True
        return False

    def poista2(self, kohta, apumuuttuja):
        for j in range(kohta, self.alkioiden_lkm - 1):
            apumuuttuja = self.lista[j]
            self.lista[j] = self.lista[j + 1]
            self.lista[j + 1] = apumuuttuja

        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]
        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lista[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lista[i]) + ", "
            tuotos = tuotos + str(self.lista[self.alkioiden_lkm - 1]) + "}"
            return tuotos
