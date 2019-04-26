import random
import os
import subprocess
import sys

def split_data_set(image_dir):

    f_val = open("../Capstone_Project_1/src/main/python/har_test.txt", 'w')
    f_train = open("../Capstone_Project_1/src/main/python/har_train.txt", 'w')
    
    for path, dirs, files in os.walk(image_dir):
        data_size = len(files)

        ind = 0
        data_test_size = int(0.1 * data_size)
        test_array = random.sample(range(data_size), k=data_test_size)

        for file in files:
            ind += 1
            
            if ind in test_array:
                f_val.write(path + '/' + file + '\n')
            else:
                f_train.write(path + '/' + file + '\n')


split_data_set(sys.argv[1])
