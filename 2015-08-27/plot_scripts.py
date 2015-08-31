from pylab import *
import numpy

ncores = numpy.arange(1,128,1)

plot(ncores, 1.0/(0.1+0.9/ncores))

show()

plot(ncores, (1.0/(0.1+0.9/ncores))/ncores)

show()
