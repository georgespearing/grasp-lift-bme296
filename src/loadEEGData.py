#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:43:03 2021

@author: george
"""

import numpy as np

def loadData(subject=1, series=1, data_directory='train'):
    
    file_path = f'{data_directory}/subj{subject}_series{series}_data.csv'
    
    # load just the data
    eegData = np.loadtxt(file_path, delimiter=',', usecols=(np.arange(1,33)), max_rows=1)
    
    # just the channel names
    channels = np.loadtxt(file_path, delimiter=',', usecols=(np.arange(1,33)), max_rows=1, dtype=str, unpack=True)
    
    # turn it into a dictionary
    data = {}
    data['eeg'] = eegData
    data['channels'] = channels