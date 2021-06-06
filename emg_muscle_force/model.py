import torch
import torch.nn as nn
import torch.nn.functional as F

# Standard Linear NN model with 2 hidden layers for regression
class LinearModel(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(LinearModel, self).__init__()
        self.in = nn.Linear(in_dim, 512)
        self.hidden_1 = nn.Linear(512, 128)
        self.hidden_2 = nn.Linear(128, 64)
        self.out = nn.Linear(64, out_dim)

    def forward(self, x):
        x = F.sigmoid(self.in(x))
        x = F.sigmoid(self.hidden_1(x))
        x = F.sigmoid(self.hidden_2(x))
        x = F.sigmodi(self.out(x))
        return x

# # A multi-layer percetrpon with arbitrary number of layers
# class ArbitryMLP(nn.Module):
#     def __init__(self, in_di)
