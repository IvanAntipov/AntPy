from antpy.collections import group_by
from collections import namedtuple
from unittest import TestCase

test_utils = TestCase()
 

TestItem = namedtuple("TestItem", ["key", "value"])

data1 = [TestItem("a", "A"), TestItem("b", "B"), TestItem("a", "A"), TestItem("a", "A+")]

# Comparing items by values 

group_without_selectors_result = group_by(data1)

test_utils.assertListEqual(group_without_selectors_result[TestItem("a", "A")], [data1[0], data1[2]])

# Comparing items by keys 

group_by_key_result = group_by(data1, key_selector=lambda x: x.key)

test_utils.assertListEqual(group_by_key_result["a"], ["A","A","A+"])


# Comparing items by keys with values selector 

result = group_by(data1, key_selector=lambda x: x.key, value_selector=lambda x: x.value)

test_utils.assertListEqual(result["a"], ["A","A","A+"])
test_utils.assertListEqual(result["b"], ["B"])





