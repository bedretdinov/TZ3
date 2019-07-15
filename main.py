from Lib import DataGenerator
from Lib import SysArguments
import pandas as pd
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os. chdir(dir_path)

arguments = SysArguments()

if(arguments.get('--help')):
    print('''
       --input_file  - Названием входного файла с данными
       --output_file - Выходной файла для записи
       --dT          - Порог времени для расчетов 
    ''')
    sys.exit(0)

dT          = arguments.get('--dT', required=True, type='float')
input_file  = arguments.get('--input_file', required=True)
output_file = arguments.get('--output_file', required=True)


obj = DataGenerator()
obj.Indexing(input_file)
res = obj.calc(dT=dT)


if(output_file):
    pd.DataFrame(res, columns=['n','result'] ).to_csv(output_file, index=None)
