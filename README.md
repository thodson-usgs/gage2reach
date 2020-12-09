# gage2reach
Look up NHDplus v2.1 reach ID for approximately 26,000 U.S. Geological Survey streagages active prior to 2012.
```python
from gage2reach import nhd_reach_id
reach_id = nhd_reach_id('03339000')
```
NHDplus reach lookup table generated using data at
https://www.sciencebase.gov/catalog/item/577445bee4b07657d1a991b6

To regenerate the reach lookup table, first pull the data from ScienceBase and unzip
```bash
wget https://www.sciencebase.gov/catalog/file/get/577445bee4b07657d1a991b6?facet=GageLoc
```
Then run the following:
```python
import pickle, bz2, shape
import shapefile
shape = shapefile.Reader("GageLoc/GageLoc.shp")

shape.records()[0]

reach_lookup_table = dict((row[9], row[2]) for row in shape.records())

with bz2.BZ2File("NHDPlus_v2.1_reach_lookup.bz2", 'w') as f:
    pickle.dump(reach_lookup_table, f)
```
