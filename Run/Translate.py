import sys


start = int(sys.argv[1])
end = int(sys.argv[2])


import numpy as np
import pandas as pd
import os
import re
import time

dir_name = 'Train Pos Data/'
Reviews = np.array(pd.read_csv(dir_name+'pos_reviews.csv', header=None))
Labels = np.array(pd.read_csv(dir_name+'pos_Labels.csv', header=None))

from googletrans import Translator

Translated_list = []

for i in range(start, end):
    translator = Translator()
    translated = translator.translate( Reviews[i][0], src='en', dest='hi').text
    tup = (Reviews[i][0], translated, Labels[i][0] )
    Translated_list.append(tup)
    

Translated_list_pandas = pd.DataFrame(Translated_list)
name = 'Results/' + str(start) + '_' + str(end) + '.csv'
Translated_list_pandas.to_csv(name,  header=None, index=False)