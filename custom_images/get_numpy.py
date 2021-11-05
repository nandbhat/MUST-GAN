from see_npy import load_mask
import glob
import json
import numpy as np
path = '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/custom_images/segmentation/*.png'
files = glob.glob(path)
for file in files:
	result = load_mask(file)
	print(result)
	np.save(file.split('.')[0], result)
