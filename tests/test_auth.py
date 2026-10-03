import unittest
from authen import hash_password, verify_password

class TestAuthentication(unittest.TestCase):
    def test_password_hashing_and_verification(self):
        pw = "secure123"
        hashed = hash_password(pw)
        self.assertTrue(verify_password(pw, hashed))
        self.assertFalse(verify_password("wrongpw", hashed))

if __name__ == '__main__':
    unittest.main()
