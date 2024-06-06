import unittest

class demo01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    def setUp(self):
        print('setup')


    def tearDown(self):
        print('teardown')


    def test_case01(self):
        print('testcase01')
        self.assertEqual(1,1,"相等")
        self.assertIn('h','this')

    def test_case02(self):
        print('testcase02')
        self.assertEqual(2,2,"相等")
        self.assertIn('h','this')

    @unittest.skipIf(2!=3,"跳过用例")
    def test_case03(self):
        print('testcase03')
        self.assertEqual(2,3,"相等")
        self.assertIn('h','this')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')


class demo02(unittest.TestCase):
    def test_case04(self):
        print('testcase04')
        self.assertEqual(2,2,"相等")
        self.assertIn('h','this')

    def test_case05(self):
        print('testcase05')
        self.assertEqual(2,2,"相等")
        self.assertIn('h','this')


class demo03(unittest.TestCase):
    def test_case06(self):
        print('testcase06')
        self.assertEqual(2,2,"相等")
        self.assertIn('h','this')


if __name__ == '__main__':
    # # 方法一：全部执行
    # unittest.main()

    # # 方法二：执行部分测试类中的部分测试方法
    # suite = unittest.TestSuite()
    # suite.addTest(demo01("test_case01"))
    # suite.addTest(demo02("test_case04"))
    #
    # unittest.TextTestRunner().run(suite)


    # # 方法三：执行部分测试方法
    # suite01 = unittest.TestLoader().loadTestsFromTestCase(demo01)
    # suite02 = unittest.TestLoader().loadTestsFromTestCase(demo03)
    # suite_all = unittest.TestSuite([suite01,suite02])
    # unittest.TextTestRunner().run(suite_all)


    # 方法四：执行全部命中某个规则的测试方法
    discover = unittest.defaultTestLoader.discover("./",'test*.py')
    unittest.TextTestRunner().run(discover)


