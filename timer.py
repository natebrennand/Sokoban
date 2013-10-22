
import time

def timeit(f):

    def timed(*args, **kw):

        t_start = time.time()
        result = f(*args, **kw)
        return result, (time.time()-t_start)

    return timed
    
