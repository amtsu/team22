"""
функции, тестирующие класс quapirow
"""
from quapirow import QuaPiRow
def test_quapirow_1():
	expected = ("-1/1","1/3","-1/5","1/7","-1/9","1/11","-1/13",
	"1/15","-1/17","1/19","-1/21","1/23","-1/25","1/27","-1/29",
	"1/31",	"-1/33","1/35","-1/37","1/39",)
	result = QuaPiRow(20)
	for element in expected:
		assert element == next(result)

