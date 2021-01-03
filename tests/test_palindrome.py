import unittest
import main


class TestPalindrome(unittest.TestCase):
    def test_word_valid(self):
        valid_words = ["Racecar", "Anna", "Civic", "Kayak", "Mom", "Refer", "Noon", "Repaper"]
        for word in valid_words:
            self.assertTrue(main.is_palindrome(word), "Valid word was found false")

    def test_word_invalid(self):
        invalid_words = ["hello", "world", "hi", "hey", "christmas", "a", "ah", "main"]
        for word in invalid_words:
            self.assertFalse(main.is_palindrome(word), "Invalid word was found True")

    def test_phrase_valid(self):
        valid_phrase = ["Step on no pets", "Top spot", "No lemon, no melon", "Was it a cat I saw", "Amore, Roma",
                        "No lemon no melon", "As I pee, sir, I see Pisa!"]
        for phrase in valid_phrase:
            self.assertTrue(main.is_palindrome(phrase), "Valid phrase was found false")

    def test_phrase_invalid(self):
        invalid_phrase = ["Hello World!", "My name is", "Is this a Palindrome", "Took a trip yesterday",
                          "Pycharm unit test", "Random Phrase"]
        for phrase in invalid_phrase:
            self.assertFalse(main.is_palindrome(phrase), "Invalid phrase was found true")

    def test_punctuation_valid(self):
        valid_phrase = ["Step,on, no, pets", "Top spot!", "No: lemon, no melon", "Was it a cat I saw?", "Amore, Roma;",
                        "No lemon! no melon!", "As I pee-sir-I see Pisa!"]
        for phrase in valid_phrase:
            self.assertTrue(main.is_palindrome(phrase), "Valid phrase was found false")

    def test_spacing(self):
        valid_phrase = ["Step,on, no,          pets", "          Top  spot!", "Nolemonnomelon"]
        for phrase in valid_phrase:
            self.assertTrue(main.is_palindrome(phrase), "Valid phrase was found false")
