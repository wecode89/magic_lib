from builtins import len, iter
from magic_lib.concurrency.workers.singleton import SingletonWorkerDispatcher


class BatchDispatch(SingletonWorkerDispatcher):
    def __init__(self, ids=None, group_size=100, max_worker=10):
        super().__init__(**{'ids': ids, 'max_worker': max_worker})
        self.groups = list(self._chunk(self.ids, group_size))

    def _chunk(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def _get_iters(self):
        iterable_list = iter(self.groups)
        return iterable_list

    def _get_count(self):
        return len(self.groups)
