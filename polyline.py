# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:38:01 2019

@author: sanja
"""
import numpy as np
import pandas as pd
import geopandas as gpd
import json
from shapely.geometry import LineString, Point

def load_data(fname, nrows):
    df = pd.read_csv(fname, nrows=nrows)
    df['traj'] = json.loads('[' + df.POLYLINE.str.cat(sep=',') + ']')
    df = df[df.traj.str.len() > 1].copy()
    df['lines'] = gpd.GeoSeries(df.traj.apply(LineString))
    return gpd.GeoDataFrame(df, geometry='lines')

df = load_data('train.csv', nrows=1000)