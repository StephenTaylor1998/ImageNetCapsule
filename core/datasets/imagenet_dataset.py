import os
from torchvision import datasets
from torchvision.transforms import transforms
from .custom_transform import *

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])


def classify_train_dataset(train_dir, transform=TinyImageNetTrainTransform):
    return datasets.ImageFolder(train_dir, transform)


# val dataset example for tiny-image-net
def classify_val_dataset(val_dir, transform=TinyImageNetvalidationTransform):
    return datasets.ImageFolder(val_dir, transform)


# test dataset example for tiny-image-net
def classify_test_dataset(testdir, transform=TinyImageNetTestTransform):
    return datasets.ImageFolder(testdir, transform)
