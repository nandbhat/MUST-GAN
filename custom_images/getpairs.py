import glob
import json
path = '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/custom_images/sample_images/*.jpg'
files = glob.glob(path)
print(files)
confidence = 0
file_type = 'jpg'
file_name1 = 'full_body_female_v2_resized.jpg'
result_file = open("test_pairs.txt", mode="w", encoding="utf-8")
for file in files:
    file_name2 = file.split('/')[-1]
    if file_name2 == file_name1:
        continue
    result = file_name1 + ',' + file_name2 + '\n'
    result_file.write(result)
result_file.close()
