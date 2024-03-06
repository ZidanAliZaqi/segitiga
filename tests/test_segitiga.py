from segitiga.segitiga import Segitiga


def test_segitiga():
    luas_segitiga = Segitiga(5, 4)
    assert luas_segitiga.hitung_luas() == 10
