import unittest,os
from ddt import ddt, data, file_data, unpack
#from ddt_demo.mycode import has_three_elements, is_a_greeting
try:
    import yaml
except ImportError:  # pragma: no cover
    have_yaml_support = False
else:
    have_yaml_support = True
    del yaml

# A good-looking decorator
needs_yaml = unittest.skipUnless(
    have_yaml_support, "Need YAML to run this test"
)


a=[
    "Hello",
    "Goodbye"
]
b={
    "unsorted_list": [ 10, 12, 15 ],
    "sorted_list": [ 15, 12, 50 ]
}
path=os.getcwd()
@ddt
class FooTestCase(unittest.TestCase):
    @needs_yaml
    @file_data(os.path.join(path,'regist.yml'))
    # @data([3, 2], [6, 3], [0, 3])
    # @unpack
    def test_file_data_yaml_dict_dict(self, start, end, value):
        self.assertLess(start, end)
        self.assertLess(value, end)
        self.assertGreater(value, start)

    # @file_data(b)
    # def test_file_data_json_list(self, value):
    #     self.assertTrue(is_a_greeting(value))

    @data([3, 2], [6, 3], [0, 3])
    @unpack
    def test_cur(self,):



if __name__ == '__main__':
    unittest.main(verbosity=2)