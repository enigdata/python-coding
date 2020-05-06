import datetime 
#import redis 
import unittest
from unittest.mock import Mock 
import pytest

# class FlightStatusTracker:
#     ALLOWED_STATUSES = {"CANCELLED", "DELAYED", "ON TIME"}

#     def __init__(self):
#         self.redis = redis.StrictRedis()

#     def change_status(self, flight, status):
#         status = status.upper()
#         if status not in self.ALLOWED_STATUSES:
#             raise ValueError(f"{status} is not a valid status.")

#         key = f"flightno: {flight}"
#         value = "{}|{}".format(
#             datetime.datetime.now().isoformat(), status
#         )
#         self.redis.set(key, value)

# @pytest.fixture 
# def tracker():
#     return FlightStatusTracker()

# def test_mock_method(tracker):
#     tracker.redis.set = Mock()
#     with pytest.raises(ValueError) as ex:
#         tracker.change_status("AC101", "lost")
#     assert ex.value.args[0] == "LOST is not a valid status."
#     assert tracker.redis.set.call_count == 0

##### Case Study
#### Vigenère cipher

def test_encode():
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, text):
        return "XECWQXUIVCRKHWA"

#Add some test cases
def test_encode_spaces():
    cipher = VigenereCipher("TRAIN ")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_lowercases():
    cipher = VigenereCipher("TRain")
    encoded = cipher.encode("encoded in python")
    assert encoded == "XECWQXUIVCRKHWA"

def test_combine_character():
    assert combine_character("E", "T") == "X" 
    assert combine_character("N", "R") == "E"

### Cipher code
class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def _code(self, text, combine_func):
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plaintext):
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        return self._code(ciphertext, separate_character)

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]


def combine_character(plain, keyword):
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord("A")
    keyword_num = ord(keyword) - ord("A")
    return chr(ord("A") + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord("A")
    keyword_num = ord(keyword) - ord("A")
    return chr(ord("A") + (cypher_num - keyword_num) % 26)