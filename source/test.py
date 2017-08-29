import unittest

import utils 

class Test_Utils(unittest.TestCase):

    def test_import_API_key(self):
        self.assertEqual(utils.import_API_key('test/api_key_valid.txt'),
                         'n3149udafn3242ikadsk234nalkj34mnapi013x')
        with self.assertRaises(ValueError):
            utils.import_API_key('test/api_key_invalid_short.txt')

        with self.assertRaises(ValueError):
            utils.import_API_key('test/api_key_invalid_long.txt')
        
        with self.assertRaises(ValueError):
            utils.import_API_key('test/api_key_invalid_spaces.txt')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Utils)
    unittest.TextTestRunner(verbosity = 2).run(suite)
