##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Hang Zhang
## Email: zhanghang0704@gmail.com
## Copyright (c) 2018
##
## This source code is licensed under the MIT-style license found in the
## LICENSE file in the root directory of this source tree
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import os
import torchvision.transforms as transforms
import torchvision.datasets as datasets

class ImageNetDataset(datasets.ImageFolder):
    BASE_DIR = "ILSVRC2012"
    def __init__(self, root=os.path.expanduser('~/.encoding/data'), transform=None,
                 target_transform=None, train=True, **kwargs):
        split='train' if train == True else 'val'
        root = os.path.join(root, self.BASE_DIR, split)
        super(ImageNetDataset, self).__init__(
            root, transform, target_transform)
