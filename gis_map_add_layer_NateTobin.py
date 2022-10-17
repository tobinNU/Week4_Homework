#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arcgis
from arcgis.gis import GIS
gis = GIS("https://nu.maps.arcgis.com/home/index.html", "tobin.n_NU")

from arcgis.features import FeatureLayer

fl = FeatureLayer(url='https://services1.arcgis.com/KUeKSLlMUcWvuPRM/arcgis/rest/services/Boston_Outline/FeatureServer/0', gis=gis)

map1 = gis.map("Boston, MA")


map1.add_layer(fl)
map1


# In[ ]:





# In[ ]:




