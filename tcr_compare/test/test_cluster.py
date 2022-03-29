
import os,sys,unittest

sys.path.insert(1, os.path.join(sys.path[0], '...'))
sys.path.insert(1, os.path.join(sys.path[0], '..'))
src_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/tcr_compare/')
sys.path.append(src_path)

import cluster

class Test(unittest.TestCase):
    def setUp(self):
        self.params = {'wdir': os.getcwd(),
            'input_file': 'vdjdb',
            'chain_selection': 'beta',
            'cpus': 1,
            'n_logos': None,
            'graphs': None,
            'annotate':None,
            'drop_nonbinders': None,
            'spike_in':None,
            'single_epitopes': None,
            'min_clustsize': 1}

        self.model_selection=['clustcr','length']
        self.params=cluster.initialise(self.params)
        self.clust = cluster.Cluster(self.params)
        self.clust.load_data()
        self.clust.get_chain_data()


#     def test_cluster(self):
#         self.clust.cluster(self.model_selection)


if __name__ == '__main__':
    unittest.main()

