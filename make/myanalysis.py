import sys, commands
try:
    inputNames = sys.argv[2:]
except:
    inputNames = 'data-1-1.dat'
try:
    outputName = sys.argv[1]
except:
    outputName = 'summary-0.dat'

print '=== myanalysis.py ==='
print 'Input :', inputNames
print 'Output :', outputName
    
f = open(outputName, 'w')
f.close()
