import os
import pickle
import bz2

package_dir, package_filename = os.path.split(__file__)

LOOKUP_FILE = 'NHDPlus_v2.1_reach_lookup.bz2'
DATA_PATH = os.path.join(package_dir, LOOKUP_FILE)

with bz2.BZ2File(DATA_PATH) as f:
    reach_lookup_table = pickle.load(f)

def nhd_reach_id(usgs_gage_id):
    """Look up NHDplus reach ID associated with a USGS streamgage.
    
    Look up NHDplus v2.1 reach ID of approximately 26,000 U.S. Geological Survey
    streamgages active prior to 2012.
    
    Data source:
    https://www.sciencebase.gov/catalog/item/577445bee4b07657d1a991b6

    Parameters
    ----------
    usgs_gage_id : str
        USGS gage ID

    Returns
    -------
    str
        NHDplus reach ID
    """
    #return(reach_lookup_table[usgs_gage_id])
    try:
        return(reach_lookup_table[usgs_gage_id])

    except KeyError as ke:
        print('No data for streamgage', ke)
        raise

