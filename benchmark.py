import time
import pprint
from collections import defaultdict


class Benchmark:
    def __init__(self):
        self.funcs = []
        self.n_funcs = 0

        self.inputs = []
        self.n_inputs = 0

    def __repr__(self):
        pass

    def set_funcs(self, *args):
        self.funcs.extend(args)
        self.n_funcs = len(args)

    def set_inputs(self, *args):
        self.inputs.extend(args)
        self.n_inputs = len(args)

    def compare(self, n=100000, display=True):
        stats = defaultdict(list)
        for i, f in enumerate(self.funcs):
            for input in self.inputs:
                times = self._run_n_times(f, input, n)
                stats[i].append([max(times), min(times), mean(times)])
        if display:
            self._display(stats)

    @staticmethod
    def _run_n_times(func, inputs, n_times):
        times = []
        for i in range(n_times):
            start = time.time()
            func(*inputs)
            time_taken = time.time() - start
            times.append(time_taken)
        return times

    @staticmethod
    def _display(times):
        # for time series will attempt to save time via interpolation
        # have option for FULL range
        pprint.pprint(times)


def mean(arr):
    return sum(arr)/len(arr)