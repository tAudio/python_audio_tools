import numpy as np

class tCore:

	#normalize  vector to -1.0 , 1.0 range, with adjustable offset
    def _norm(self, data, offset=0):
        min_v = min(data)
        max_v = max(data)
        offset = min_v+max_v
        data = data+(offset/2)
        data = np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1
        return (data * ((max_v/min_v)*-1))+offset

    def _simple_norm(self, data, offset=0):
        min_v = min(data)
        max_v = max(data)
        return np.array([((x-min_v) / (max_v-min_v)) for x in data])+offset

    def _timevector(self, length, sample_rate):
	    return np.arange(0,length,1.0/sample_rate)