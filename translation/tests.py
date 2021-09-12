import unittest

from templatetags.translate_extras import translate
from setup_logger import test_logger


# TODO: RUN MORE TESTS

class TestTranslate(unittest.TestCase):

    def test_translate_extras(self):
        test_logger.info(" 'translate' Function Test Started")
        word = translate("jasm")
        self.assertEqual(word, 'جاسم')
        self.assertNotEqual(word, "Jasm")
        self.assertIsInstance(word, str)
        test_logger.info(" Test Ended")

if __name__ == '__main__':
    unittest.main()
