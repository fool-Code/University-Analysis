import geopandas as gpd
import contextily as cx
import numpy as np
import sys
from matplotlib import pylab as plt


sys.path.append('/home/carlos/repos/commuters/functions')
from return_g_estado import *

# brasil_map = gpd.read_file('BR_UF_2021/BR_UF_2021.shp')

# Read path shapefile map with geopandas 
def map_sh(path_map: str) -> any:
    """Return path file readded 
    
    Parameters
    ----------
    path_map : string
        Path to the desirable shapefile map
    """    
    try:
        return gpd.read_file(path_map)
    except TypeError:
        raise TypeError


def return_net_graph(estado: str, path_map_1: str, scale: int =100, with_labels:bool=True) -> None:
    """Plot network graph with map 
    Using city as nodes and edges as the link between source city to the target city
    Parameters
    ----------
    estado : string 
            State abbreviation

    path_map_1 : string 
                Path to the desirable shapefile map

    scale : integer 
            Number that multiply the array node size 

    with_labels : bool
                Whether or not have city name (node labels)
    """
    map_sh_readded = map_sh(path_map_1)
    g_ = return_g_estado(estado)
    pos_nx = {}
    name_nx = {}
    node_colour = '#b2e2e2'     
    edge_colour = '#252525'
    font_colour = '#202020'
    # Take each zip code from data info and make a position based on longitude and latitude 
    for zip_code in list(g_.nodes()):
        pos_nx[zip_code] = tuple(info[info.CODE==zip_code][['LON','LAT']].values[0])
        name_nx[zip_code] = info[info.CODE==zip_code].CITY.values[0]


    f, ax = plt.subplots(figsize=(10*2,7*2))
    if estado=='all':
        map_sh_readded.plot(ax=ax, color='#bdbdbd')
    else:
        # map_sh_readded.plot(ax=ax, color='#f0f0f0',zorder=0color='#bdbdbd')
        map_sh_readded[map_sh_readded.SIGLA==estado].plot(ax=ax, alpha=0.3, edgecolor='k')
        cx.add_basemap(ax, crs=map_sh_readded.crs)

    
    # Make a network draw with networkx using the return_g_estado function 
    nx.draw_networkx(g_,
                    pos=pos_nx,
                    node_size=(scale*np.asarray(list(dict(g_.degree()).values()))).tolist(), #(50*np.asarray(dict(g_.degree()).values())+30).tolist(),
                    labels=name_nx,
                    node_color=node_colour,                    
                    edge_color=edge_colour,
                    alpha=1,
                    width=2,
                    style='dotted',
                    font_size=12,
                    font_color=font_colour,
                    with_labels=with_labels,
                    ax=ax)
    ax.axis('off')
    plt.savefig(f'../figures/{estado}.png')
