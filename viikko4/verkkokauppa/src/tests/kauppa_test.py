import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.saldot = {1: 10, 2: 10}
        self.tuotteet = {1: Tuote(1, "maito", 5), 2: Tuote(2, "leipä", 3)}

        # tehdään toteutus saldo-metodille
        def varasto_saldo(id):
            return self.saldot.get(id, 0)

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(id):
            return self.tuotteet.get(id)

        self.varasto_mock = Mock()

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tilimaksu_kutsuu_tilisiirtoa_oikeilla_argumenteilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_tilimaksu_kahdella_eri_tuotteella_kutsuu_tilisiirtoa_oikeilla_argumenteilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_tilimaksu_kahdella_samalla_tuotteella_kutsuu_tilisiirtoa_oikeilla_argumenteilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_tilimaksu_kun_toinen_tuote_loppu_kutsuu_tilisiirtoa_oikeilla_argumenteilla(self):
        self.saldot[2] = 0

        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_pyydetaan_uusi_viite_jokaisessa_tilimaksussa(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

        self.assertEqual(
            [kutsu.args[1] for kutsu in self.pankki_mock.tilisiirto.call_args_list],
            [1, 2, 3],
        )

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_with(self.tuotteet[1])

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)


class TestTuote(unittest.TestCase):
    def test_samalla_idlla_olevat_tuotteet_ovat_yhtavaria(self):
        self.assertEqual(Tuote(1, "maito", 5), Tuote(1, "leipa", 3))

    def test_samalla_idlla_oleville_tuotteille_sama_hash(self):
        self.assertEqual(hash(Tuote(1, "maito", 5)), hash(Tuote(1, "leipa", 3)))

    def test_tuotteen_merkkijonoesitys_on_tuotteen_nimi(self):
        self.assertEqual(str(Tuote(1, "maito", 5)), "maito")
