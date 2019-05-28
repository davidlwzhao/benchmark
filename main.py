from examples import search
import benchmark as bm
import cProfile as profile
from functools import wraps

def test_func():
    for i in range(100):
        x = i ** 3


if __name__ == '__main__':
    benchmark = bm.Benchmark()
    benchmark.set_funcs(search.search1, search.search2, search.search3)
    benchmark.set_inputs(search.search_inputs, search.search_inputs2)
    benchmark.compare(10)

    code = compile(test_func, '<string>', 'exec')
    profile.run(code)