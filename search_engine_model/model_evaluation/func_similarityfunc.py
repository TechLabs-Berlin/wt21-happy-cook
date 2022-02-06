import numpy as np
from scipy.spatial.distance import euclidean


def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim

def euclidean_sim(a,b):
    return euclidean(a,b)