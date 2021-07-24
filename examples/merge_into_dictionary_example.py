from antpy.collections import merge_dictionaries, merge_into_dictionary
from collections import namedtuple

from unittest import TestCase

test_utils = TestCase()
 
TestItem = namedtuple("TestItem", ["key", "value"])

data1 = [TestItem("a", "A"), TestItem("b", "B"), TestItem("c", "C")]

data2 = [("a", 1), TestItem("b", 2)]

data3 = [("a", "a+"), TestItem("c", "c+")]

accumulator = {}

merge_into_dictionary(accumulator_dict=accumulator, seq_to_join=data1, property="field1", key_selector=lambda x: x.key, value_selector=lambda x: x.value)
merge_into_dictionary(accumulator_dict=accumulator, seq_to_join=data2, property="field2", key_selector=lambda x: x[0], value_selector=lambda x: x[1])
merge_into_dictionary(accumulator_dict=accumulator, seq_to_join=data3, property="field3", key_selector=lambda x: x[0], value_selector=lambda x: x[1])


accumulator

# >>> accumulator
#    {'a': {'field1': 'A', 'field2': 1, 'field3': 'a+'}, 'b': {'field1': 'B', 'field2': 2}, 'c': {'field1': 'C', 'field3': 'c+'}}