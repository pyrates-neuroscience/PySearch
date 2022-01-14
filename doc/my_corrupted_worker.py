"""
Cluster worker raising a SyntaxError in line 14 since pd.DataFrame.loc is called using "()" instead of "[]"
"""

from pyrates.utility_old.grid_search import ClusterWorkerTemplate
from scipy.signal import welch


class MyWorker(ClusterWorkerTemplate):
    def worker_postprocessing(self, **worker_kwargs):
        for idx, data in self.results.iteritems():
            t = self.results.index.to_list()
            dt = t[1] - t[0]
            f, p = welch(data.to_numpy(), fs=1/dt, axis=0)
            # self.processed_results.loc(:, idx) = p  # wrong
            self.processed_results.loc[:, idx] = p  # correct
        self.processed_results.index = f


if __name__ == "__main__":
    cgs_worker = MyWorker()
    cgs_worker.worker_init()

