import unittest


class Pangram():
    def checkPangram(pangram_text):
        for i in range(65, 91):
            if not (str(pangram_text).upper()).__contains__(chr(i)):
                return False
        return True

    def checkPangramList(the_list):
        list_of_pangrams = []
        index = 0
        for pangram_text in the_list:
            list_of_pangrams.append(Pangram.checkPangram(pangram_text))

        return list_of_pangrams

class PangramTest(unittest.TestCase):

    def setUp(self):
        self.temp = Pangram

    def test_panagram_one_string_positive(self):
        str = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(True, self.temp.checkPangram(str))

    def test_non_panagram_one_string(self):
        str = "The brown fox jumps over the lazy dog"
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_number_as_string_input_for_pangram(self):
        str = "1111"
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_number_as_number_input_for_pangram(self):
        str = 1111
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_number_as_minus_number_input_for_pangram(self):
        str = -1111
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_number_as_float_number_input_for_pangram(self):
        str = 1111.1111
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_empty_input_for_pangram(self):
        str = ""
        self.assertEqual(False, self.temp.checkPangram(str))

    def test_pangram_list_input_for_pangram(self):
        str = ["The quick brown fox jumps over the lazy dog",
                "Pack my box with five dozen liquor jugs",
                "Sphinx of black quartz; judge my vow",
                "Jackdaws love my big sphinx of quartz"]
        self.assertEqual([True, True, True, True], self.temp.checkPangramList(str))

    def test_non_pangram_list_input_for_pangram(self):
        str = [
                "The brown fox jumps over the lazy dog",
                "Pack my with five dozen liquor jugs",
                "Sphinx of quartz; judge my vow",
                "Jackdaws love my sphinx of quartz"]
        self.assertEqual([False, False, False, False], self.temp.checkPangramList(str))

    def test_non_pangram_list_with_numbers_input_for_pangram(self):
        str = [
                "The brown fox jumps over the lazy dog",
                "Pack my with five dozen liquor jugs",
                1234,
                "Jackdaws love my sphinx of quartz"]
        self.assertEqual([False, False, False, False], self.temp.checkPangramList(str))

    def tearDown(self):
        self.temp = None
