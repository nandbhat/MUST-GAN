import numpy as np
import sys
from PIL import Image
import torchvision.transforms as transforms
import copy
from human_parsing_label import get_label_map
import torch


# path = '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/datasets/semantic_merge3/WOMEN/Cardigans/id_00000010/01_1_front_vis.png'
path = '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/custom_images/segmentation/full_body_female_v2_resized.png'
result = np.load(
    '/mnt/hdd0/nandan/active/must-gan/MUST-GAN/custom_images/segmentation/full_body_female_v2_resized.npy')
np.set_printoptions(threshold=sys.maxsize)


def load_mask(file_path):
    mask = Image.open(file_path)
    # resize = transforms.Resize((256, 176))
    # mask = resize(mask)
    mask = torch.from_numpy(np.array(mask))
    aiyu2atr, atr2aiyu = get_label_map(8)

    texture_mask = copy.deepcopy(mask)
    for atr in atr2aiyu:
        aiyu = atr2aiyu[atr]
        texture_mask[mask == atr] = aiyu
    return texture_mask.cpu().detach().numpy()

torch.set_printoptions(profile="full")
# print(load_mask(path))
print('\n\n\n\n\n >>>>>>>>>>>>>>>>>>> \n\n\n\n\n')
print(result)

