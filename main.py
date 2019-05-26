from examples import search
import benchmark as bm

if __name__ == '__main__':
    benchmark = bm.Benchmark()
    benchmark.set_funcs(search.search1, search.search2, search.search3)
    benchmark.set_inputs(search.search_inputs, search.search_inputs2)
    benchmark.compare(10)