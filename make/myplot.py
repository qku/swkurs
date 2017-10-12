import sys, commands
try:
    inputName = sys.argv[1]
except:
    inputName = 'summary-0.dat'
try:
    outputName = sys.argv[2]
except:
    outputName = 'figure-0.dat'

print '==== myplot ===='
print 'Input: ', inputName
print 'Output: ', outputName
    
f = open(outputName, 'w')
f.close()
