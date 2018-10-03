import unittest
from data_handler import DataHandler


dh = DataHandler('../../DAL/Files.db')
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



if __name__ == '__main__':
    unittest.main()