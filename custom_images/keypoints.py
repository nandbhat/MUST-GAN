import glob
import json
path = '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/custom_images/json/*.json'
files = glob.glob(path)
print(files)
confidence = 0
file_type = 'jpg'
result_file = open("keypoints_result.txt", mode="w", encoding="utf-8")
for file in files:
    f = open(file, 'r')
    data = json.load(f)
    print(data)
    detected_points = data['people'][0]['pose_keypoints_2d']
    x = list()
    y = list()
    for index, point in enumerate(detected_points):
        if ((index) % 3 == 0):
            print(point)
            x.append(point)
            y.append(detected_points[index + 1])
    print(x)
    print(y)
    x = [-1 if item == 0 else item for item in x]
    y = [-1 if item == 0 else item for item in y]
    x = [round(item) for item in x]
    y = [round(item) for item in y]
    file_name = (file.split('/')[-1].split('.')[0]
                 ).split('_')[0] + '.' + file_type
    joined_x = '[' + ', '.join(map(str, x)) + ']'
    joined_y = '[' + ', '.join(map(str, y)) + ']'
    result = file_name + ':' + joined_y + ':' + joined_x + '\n'
    result_file.write(result)
    print(result)
    f.close()
result_file.close()
