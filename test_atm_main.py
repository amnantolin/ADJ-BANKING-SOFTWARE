import unittest
from client_data_handler import DataHandler

dh = DataHandler('../../DAL/Files.db')
class TestClient_Data_Handler(unittest.TestCase):

    def test_client_log(self):
        print("test_client_log")
        self.assertTrue(dh.client_log(1111111111111111, 111111))
        self.assertTrue(dh.client_log(2222222222222222, 222222))
        self.assertTrue(dh.client_log(3333333333333333, 333333))
        self.assertFalse(dh.client_log(4444444444444444, 444444))

    def test_view_anum(self):
        print("test_view_anum")
        self.assertIsNotNone(dh.view_anum(1111111111111111))
        self.assertEqual(111111111111, dh.view_anum(1111111111111111)[0])
        self.assertIsNotNone(dh.view_anum(2222222222222222))
        self.assertEqual(222222222222, dh.view_anum(2222222222222222)[0])
        self.assertIsNotNone(dh.view_anum(3333333333333333))
        self.assertEqual(333333333333, dh.view_anum(3333333333333333)[0])
        self.assertIsNone(dh.view_anum(4444444444444444))

    def test_get_bal(self):
        print("test_get_bal")
        self.assertIsNotNone(dh.get_bal(111111111111))
        self.assertEqual(1000, dh.get_bal(111111111111)[0])
        self.assertIsNotNone(dh.get_bal(222222222222))
        self.assertEqual(10000, dh.get_bal(222222222222)[0])
        self.assertIsNotNone(dh.get_bal(333333333333))
        self.assertEqual(9999999, dh.get_bal(333333333333)[0])
        self.assertIsNone(dh.get_bal(444444444444))

    def test_update_bal(self):
        print("test_update_bal")
        self.assertEqual(1000, dh.get_bal(111111111111)[0])
        dh.update_bal(2000, 111111111111)
        self.assertEqual(2000, dh.get_bal(111111111111)[0])
        dh.update_bal(1000, 111111111111)
        self.assertEqual(1000, dh.get_bal(111111111111)[0])

        self.assertEqual(10000, dh.get_bal(222222222222)[0])
        dh.update_bal(20000, 222222222222)
        self.assertEqual(20000, dh.get_bal(222222222222)[0])
        dh.update_bal(10000, 222222222222)
        self.assertEqual(10000, dh.get_bal(222222222222)[0])

    def test_get_pin(self):
        print("test_get_pin")
        self.assertIsNotNone(dh.get_pin(111111111111))
        self.assertEqual(111111, dh.get_pin(111111111111)[0])
        self.assertIsNotNone(dh.get_pin(222222222222))
        self.assertEqual(222222, dh.get_pin(222222222222)[0])
        self.assertIsNotNone(dh.get_pin(333333333333))
        self.assertEqual(333333, dh.get_pin(333333333333)[0])
        self.assertIsNone(dh.get_pin(444444444444))

    def test_update_pin(self):
        print("test_update_pin")
        self.assertEqual(111111, dh.get_pin(111111111111)[0])
        dh.update_pin(222222, 111111111111)
        self.assertEqual(222222, dh.get_pin(111111111111)[0])
        dh.update_pin(111111, 111111111111)
        self.assertEqual(111111, dh.get_pin(111111111111)[0])

        self.assertEqual(222222, dh.get_pin(222222222222)[0])
        dh.update_pin(333333, 222222222222)
        self.assertEqual(333333, dh.get_pin(222222222222)[0])
        dh.update_pin(222222, 222222222222)
        self.assertEqual(222222, dh.get_pin(222222222222)[0])



if __name__ == '__main__':
    unittest.main()


