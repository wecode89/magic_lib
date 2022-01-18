import concurrent.futures
import os
from tqdm import tqdm
from magic_lib.misc.log import get_logger
from magic_lib.concurrency.workers.template import TemplateWorkerDispatcher


logger = get_logger(os.path.basename(__file__), level=os.environ.get('LOG_LEVEL', 'DEBUG'))


class SingletonWorkerDispatcher(TemplateWorkerDispatcher):
    def __init__(self,  ids=None, max_worker=10):
        self.ids = ids
        self.max_worker=max_worker

    def run(self):
        # dispatch
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_worker) as executor:
            output = list(tqdm(executor.map(self._singleton, self._get_iters()), total=self._get_count()))

        # result
        worker_result = self._collect(output)

        # sort
        worker_result = self._sort(worker_result)
        logger.debug("worker_result---> {}".format(worker_result))
        return worker_result

    def _get_iters(self):
        iterable_list = iter(list(self.ids))
        return iterable_list

    def _get_count(self):
        return len(self.ids)

    def _collect(self, output):
        # collect result
        result = [x for x in output if x]

        # merge (if item is list)
        merged = []
        for x in result:
            if isinstance(x, list):
                merged.extend(x)
            else:
                merged.append(x)
        return merged

    def _sort(self, result):
        return result

    def _singleton(self, symbol):
        raise Exception("Not Implemented")