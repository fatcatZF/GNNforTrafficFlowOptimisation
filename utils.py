import numpy as np
import torch
import torch.nn as nn
import networkx as nx


def create_edgeNode_relation(dg):
    """
    args:
        dg: a networkx DiGraph object
    """
    n_edges = dg.number_of_edges()
    n_nodes = dg.number_of_nodes()
    rel_rec = np.zeros((n_edges, n_nodes))
    rel_send = np.zeros((n_edges, n_nodes))
    senders = np.array([e[0] for e in dg.edges])
    receivers = np.array([e[1] for e in dg.edges])
    rel_send[range(n_edges), senders]=1
    rel_rec[range(n_edges), receivers]=1
    rel_rec = torch.from_numpy(rel_rec)
    rel_send = torch.from_numpy(rel_send)

    return rel_rec.float(), rel_send.float()




