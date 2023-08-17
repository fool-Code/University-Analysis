import pandas as pd
import networkx as nx
from networkx import subgraph

edges = pd.read_csv('data/br_commuters.csv')
info = pd.read_csv('data/br_info.csv')


def return_g_estado(estado:  str) -> subgraph: 
    """Returns the subgraph induced on nodes

    Parameters
    ----------
    estado : string 
            State abbreviation
    """
    if estado == 'all':
        df_ = edges
    else:
        df_ = edges[edges.source.isin(info[info.STATE==estado].CODE.unique()) & edges.target.isin(info[info.STATE==estado].CODE.unique())]
    g_ =  nx.from_pandas_edgelist(df=df_, edge_attr='weight')
    
    
    Gcc = sorted(nx.connected_components(g_), key=len, reverse=True)
    gg_ = g_.subgraph(Gcc[0])
    return gg_