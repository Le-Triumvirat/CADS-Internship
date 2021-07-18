import torch

import dgl
from dgl.data import CoraGraphDataset


print(torch.tensor([1059,1069,1074]))
data_ = CoraGraphDataset()
print(data_.num_classes)