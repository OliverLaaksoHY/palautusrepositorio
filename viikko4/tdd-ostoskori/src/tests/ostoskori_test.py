import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipa", 2)

    def lisaa_maito(self):
        self.kori.lisaa_tuote(self.maito)

    def lisaa_leipa(self):
        self.kori.lisaa_tuote(self.leipa)

    def assert_kori_on_tyhja(self):
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.lisaa_maito()

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_on_tuotteen_hinta(self):
        self.lisaa_maito()

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.lisaa_maito()
        self.lisaa_leipa()

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_on_hintojen_summa(self):
        self.lisaa_maito()
        self.lisaa_leipa()

        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.lisaa_maito()
        self.lisaa_maito()

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_kaksi_kertaa_hinta(self):
        self.lisaa_maito()
        self.lisaa_maito()

        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.lisaa_maito()

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoksen_nimi_ja_lukumaara_ovat_oikeat(self):
        self.lisaa_maito()

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.lisaa_maito()
        self.lisaa_leipa()

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_tasan_yksi_ostos(self):
        self.lisaa_maito()
        self.lisaa_maito()

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoksen_nimi_ja_lukumaara_ovat_oikeat(self):
        self.lisaa_maito()
        self.lisaa_maito()

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)

    def test_kahden_saman_tuotteen_poistamisen_jalkeen_ostoksella_on_yksi_tuote(self):
        self.lisaa_maito()
        self.lisaa_maito()

        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_tuotteen_poistamisen_jalkeen_kori_on_tyhja(self):
        self.lisaa_maito()

        self.kori.poista_tuote(self.maito)

        self.assert_kori_on_tyhja()

    def test_tyhjenna_tyhjentaa_korin(self):
        self.lisaa_maito()
        self.lisaa_leipa()

        self.kori.tyhjenna()

        self.assert_kori_on_tyhja()
