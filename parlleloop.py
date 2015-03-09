from joblib import Parallel, delayed  
import multiprocessing,timeit,time
inputs = range(10)  
def processInput(i):  
    print i * i
num_cores = multiprocessing.cpu_count()

if __name__ == '__main__':
	t1=time.ctime()
	Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)
	for i in inputs:
		print i*i
	