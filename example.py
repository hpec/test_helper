from test_helper import PublicTest

x = 1
y = 2

PublicTest.assertEquals(x, 1)
PublicTest.assertEquals(x + 1, 2)
PublicTest.assertEquals(y, 1, "y is incorrect")

PublicTest.assertEqualsHashed(x,'356a192b7913b04c54574d18c28d46e6395428ab')

PublicTest.printStats()

PublicTest.setFailFast()
PublicTest.setPrivateMode()
PublicTest.assertEquals(y, 1, "y is incorrect")
