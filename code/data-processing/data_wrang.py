import os
import glob
import xarray as xr
import rioxarray

import geopandas as gpd
from shapely.geometry import box

import pandas as pd
import numpy as np

import h5py
!export HDF5_USE_FILE_LOCKING=FALSE

from typing import List

local_dir = '/home/jovyan/data-store'

import zarr


def gen_chelsa_ds(
    chelsa: List[str], bbox: List[float]
):
    """Clip and merge a selection of CHELSA NetCDF files into geozarr.

    Args:
        chelsa: List of CHELSA NetCDF file locations
        bbox: Bounding box coordinates (xmin, ymin, xmax, ymax)

    Returns:
        Concatenated and bbox clipped DataSet of all input CHELSA NetCDFs
    """
    xmin, ymin, xmax, ymax = bbox

    ## Add optional date filtering here
    dates = [a.split('_')[-1].split('.')[0] for a in chelsa]
    years = [int(d[:4]) for d in dates]
    months = [int(d[4:]) for d in dates]
    
    chelsa_df = pd.DataFrame({'file':chelsa,
                                  'year':years,
                                  'month':months})
    ##
    ds_holder = []
    first = True
    # Read the lat/lon filtered CHELSA data into a list
    for i, row in chelsa_df.iterrows():
        dat = xr.open_dataset(row.file)
        dat.rio.write_crs(4326, inplace = True)
        # Ensure there's no misalignment between the lat/lon coord values
        if first:
            lat_coords = dat.lat.values
            lon_coords = dat.lon.values
            first = False
        dat = dat.assign_coords({'lat':lat_coords, 'lon':lon_coords})
        ds_holder.append(dat.sel(lat=slice(ymin, ymax), lon=slice(xmin, xmax)).load())
    
    # Concatenate to a single dataset
    return xr.concat(ds_holder, dim='time')