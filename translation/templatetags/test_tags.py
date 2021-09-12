import unittest

from translate_extras import translate



# TODO: RUN MORE TESTS

class TestTranslate(unittest.TestCase):

    def test_translate_extras(self):
        word = translate("jasm")
        self.assertEqual(word, 'جاسم')


if __name__ == '__main__':
    unittest.main()
