import glob
import errno
import re
import pandas as pd
import numpy as np
a = []
b = []
data = []
data1 = []
path = 'C:/Users/yadav.rishi/Desktop/Wire/*.txt'
files = glob.glob(path)
for line in files:
#    try:
        with open(line,'r',errors = 'replace') as fh:
            for line in fh.readlines():
                data = re.findall("(?<=[AZaz])?(?!.\d*=)[0-9.+-]+",line)
                a = len(data)
                b = a - round(a/20)
                if data != [] and data != ['.'] and len(data) > b :
                    data1.append(data)
                    print(data1)
df = pd.DataFrame(data1)
