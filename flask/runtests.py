import requests






import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_ola1(self):
        r = requests.get('http://localhost:5000/ola/marcio')
        self.assertEqual(r.text,'ola marcio')
        r = requests.get('http://localhost:5000/ola/mario')
        self.assertEqual(r.text,'ola mario')
    
    def test_001_ola2(self):
        r = requests.get('http://localhost:5000/ola_upgrade?pessoa1=marcio&pessoa2=alvaro')
        self.assertEqual(r.text,'ola marcio e alvaro')
        r = requests.get('http://localhost:5000/ola_upgrade?pessoa2=alvaro&pessoa1=marcio')
        self.assertEqual(r.text,'ola marcio e alvaro')
        r = requests.get('http://localhost:5000/ola_upgrade?pessoa2=robin&pessoa1=batman')
        self.assertEqual(r.text,'ola batman e robin')

    def test_002_ola3(self):
        r = requests.post('http://localhost:5000/ola_upgrade', json={'pessoa1':'batman','pessoa2':'robin'})
        self.assertEqual(r.text,'ola batman e robin')
        r = requests.post('http://localhost:5000/ola_upgrade', json={'pessoa1':'tonico','pessoa2':'tinoco'})
        self.assertEqual(r.text,'ola tonico e tinoco')

    def test_003_pega_review(self):
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt0076759/marcos')
        self.assertEqual(r.json(),{'user_id':'marcos','comment':'gostei'})
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt0076759/lucio')
        self.assertEqual(r.json(),{'user_id':'lucio','comment':'achei legal'})
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt1211837/lucio')
        self.assertEqual(r.json(),{'user_id':'lucio','comment':'estranho'})
    
    def test_004_pega_review_com_erro(self):
        r = requests.get('http://localhost:5001/socialfilm/reviews/outro/gato')
        self.assertEqual(r.json(),{'erro':'comentario nao encontrado'})
        self.assertEqual(r.status_code,404)

    def test_005_adiciona_review(self):
        r = requests.put('http://localhost:5001/socialfilm/reviews/tt1211837/marcos',
                json={'comment':'esquisito mesmo'})
        self.assertEqual(r.json()['user_id'],'marcos')
        self.assertEqual(r.json()['comment'],'esquisito mesmo')
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt1211837/marcos')
        self.assertEqual(r.json(),{'user_id':'marcos','comment':'esquisito mesmo'})
        r = requests.put('http://localhost:5001/socialfilm/reviews/tt0087332/marcos',
                json={'comment':'curiosa mistura de fantasmas e empreendedorismo'})
        self.assertEqual(r.json()['user_id'],'marcos')
        self.assertEqual(r.json()['comment'],'curiosa mistura de fantasmas e empreendedorismo')
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt0087332/marcos')
        self.assertEqual(r.json()['user_id'],'marcos')
        self.assertEqual(r.json()['comment'],'curiosa mistura de fantasmas e empreendedorismo')


    def test_006_muda_review(self):
        antes = self.total_reviews()
        r = requests.put('http://localhost:5001/socialfilm/reviews/tt0087332/marcos',
                json={'comment':'mudei de ideia. Nao gosto de fantasmas'})
        self.assertEqual(r.json()['user_id'],'marcos')
        self.assertEqual(r.json()['comment'],'mudei de ideia. Nao gosto de fantasmas')
        r = requests.get('http://localhost:5001/socialfilm/reviews/tt0087332/marcos')
        self.assertEqual(r.json()['user_id'],'marcos')
        self.assertEqual(r.json()['comment'],'mudei de ideia. Nao gosto de fantasmas')
        depois = self.total_reviews()
        self.assertEqual(antes,depois)

    def test_007_filme_invalido(self):
        r = requests.put('http://localhost:5001/socialfilm/reviews/jamesbond/marcos',
                json={'comment':'mudei de ideia. Nao gosto de fantasmas'})
        self.assertEqual(r.json()['error'],'filme nao encontrado')
        self.assertEqual(r.status_code,404)

    def total_reviews(self):
        r = requests.get('http://localhost:5001/socialfilm/all')
        return len(r.json()['reviews'])


        #postman /socialfilm/all
    

    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

if __name__ == '__main__':
    runTests()