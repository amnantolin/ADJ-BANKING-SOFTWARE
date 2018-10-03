import unittest
import sys
sys.path.insert(0, '../DAL')
from data_handler import DataHandler

dh = DataHandler('../../Database/Files.db')
class TestData_Handler(unittest.TestCase):

    def test_add_acc(self):
        print("test_add_acc")
        self.assertFalse(dh.check_reps(999999999999, 999999999999999))
        dh.add_acc(999999999999999, 999999999999, 9999, "Chris", "Robert", "Evans", "37", "09154848488",
                             "crevans@gmail.com", "Boston", 10000)
        self.assertTrue(dh.check_reps(999999999999, 999999999999999))

    def test_delete_acc(self):
        print("test_delete_acc")
        self.assertTrue(dh.find_acc(999999999999))
        dh.delete_acc(999999999999)
        self.assertFalse(dh.find_acc(999999999999))

    def test_admin_log(self):
        print("test_admin_log")
        self.assertTrue(dh.admin_log("admin", "admin"))
        self.assertTrue(dh.admin_log("amnantolin", "antolin"))
        self.assertTrue(dh.admin_log("dnojawod", "jawod"))
        self.assertTrue(dh.admin_log("jmdreyes", "reyes"))
        self.assertFalse(dh.admin_log("crevans", "evans"))

    def test_find_acc(self):
        print("test_find_acc")
        self.assertTrue(dh.find_acc(111111111111))
        self.assertTrue(dh.find_acc(222222222222))
        self.assertTrue(dh.find_acc(333333333333))
        self.assertFalse(dh.find_acc(565165155545))


    def test_view_info(self):
        print("test_view_info")
        self.assertIsNotNone(dh.view_info(111111111111))
        self.assertEqual(111111111111, dh.view_info(111111111111)[0])
        self.assertEqual("Arryll Mori", dh.view_info(111111111111)[1])
        self.assertEqual("Natividad", dh.view_info(111111111111)[2])
        self.assertEqual("Antolin", dh.view_info(111111111111)[3])
        self.assertEqual("69", dh.view_info(111111111111)[4])
        self.assertEqual("09531361651", dh.view_info(111111111111)[5])
        self.assertEqual("arryll07@gmail.com", dh.view_info(111111111111)[6])
        self.assertEqual("Bulacan", dh.view_info(111111111111)[7])
        self.assertEqual(1000, dh.view_info(111111111111)[8])
        self.assertIsNone(dh.view_info(651654646454))

    def test_view_info1(self):
        print("test_view_info1")
        self.assertIsNotNone(dh.view_info1(111111111111))
        self.assertEqual(1111111111111111, dh.view_info1(111111111111)[0])
        self.assertIsNotNone(dh.view_info1(222222222222))
        self.assertEqual(2222222222222222, dh.view_info1(222222222222)[0])
        self.assertIsNotNone(dh.view_info1(333333333333))
        self.assertEqual(3333333333333333, dh.view_info1(333333333333)[0])
        self.assertIsNone(dh.view_info1(651654646454))


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