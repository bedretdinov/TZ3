
from tqdm import tqdm
import numpy as np
from pathlib import Path
import os
import csv

class DataGenerator:
    data = {}
    file = None
    index = {'features': {}}

    def Indexing(self, file: str) -> None:

        if (not os.path.exists(file)):
            raise Exception('file {} not exist'.format(file))

        with open(file, newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=',')
            i = -1
            for line in spamreader:
                i += 1
                if (i == 0):
                    continue

                row = {}
                row['time'] = float(line[-1])
                row['feature2'] = int(line[-2])
                row['feature1'] = int(line[-3])

                self.data.update({i: row})

                try:
                    self.index['features'][(row['feature1'], row['feature2'])].append(row['time'])
                except KeyError:
                    self.index['features'].update({(row['feature1'], row['feature2']): [row['time']]})

    def calc(self, dT: float) -> list:

        result = []

        for key in tqdm(self.data):

            row = self.data[key]

            times = self.index['features'][(row['feature1'], row['feature2'])]
            count_ = 0

            for v in times:
                item_time = v

                if (item_time < row['time']):
                    if ((row['time'] - item_time) < dT):
                        count_ += 1

            result.append([key, count_])

        return result





import sys

class SysArguments:

    arguments = {}

    def __init__(self):
        for x in sys.argv[1:]:
            if(x.find('=')==-1):
                spl = [x,1]
            else:
                spl = x.split('=')

            self.arguments.update({spl[0]: spl[1]})

    def get(self,name, required=False, type='str'):

        if(name in self.arguments.keys()):
            if( type =='str'):
                return str(self.arguments[name])
            elif(type =='int'):
                return int(self.arguments[name])
            elif(type == 'float'):
                return float(self.arguments[name])
        else:
            if(required):
                raise  Exception(" required argument {}".format(name))
            else:
                return False