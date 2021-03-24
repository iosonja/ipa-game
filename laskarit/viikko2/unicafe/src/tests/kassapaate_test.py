import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    # Käteisostot:

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)
    
    def test_oliomuuttujat_ovat_alussa_oikein(self):
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_edullinen_lounas_veloittuu_oikein_jos_kateismaksu_riittaa(self):
        self.kassa.syo_edullisesti_kateisella(400)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100240)

    def test_maukas_lounas_veloittuu_oikein_jos_kateismaksu_riittaa(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100400)

    def test_kateisella_myyty_edullinen_lounas_tilastoituu_oikein(self):
        self.kassa.syo_edullisesti_kateisella(400)
        edulliset = self.kassa.edulliset
        self.assertEqual(edulliset, 1)

    def test_kateisella_myyty_maukas_lounas_tilastoituu_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        maukkaat = self.kassa.maukkaat
        self.assertEqual(maukkaat, 1)

    def test_edullisesta_lounaasta_ei_veloiteta_jos_kateismaksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(30)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_maukkaasta_lounaasta_ei_veloiteta_jos_kateismaksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(50)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100000)

    def test_edulliset_lounaat_eivat_tilastoidu_jos_kateismaksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(30)
        edulliset = self.kassa.edulliset
        self.assertEqual(edulliset, 0)

    def test_maukkaat_lounaat_eivat_tilastoidu_jos_kateismaksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(50)
        maukkaat = self.kassa.maukkaat
        self.assertEqual(maukkaat, 0)

    # Korttiostot:

    def test_edullinen_lounas_veloitetaan_kortilta(self):
        success = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(success, True)

    def test_maukas_lounas_veloitetaan_kortilta(self):
        success = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(success, True)

    def test_edullista_lounasta_ei_veloiteta_jos_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        success = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(success, False)

    def test_maukasta_lounasta_ei_veloiteta_jos_saldo_ei_riita(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        success = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(success, False)

    def test_positiivisen_summan_lataus_nakyy_kassassa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 600)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100600)

    def test_negatiivisen_summan_lataus_ei_nay_kassassa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -600)
        rahaa = self.kassa.kassassa_rahaa
        self.assertEqual(rahaa, 100000)