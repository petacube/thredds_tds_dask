#navigated to GUI at http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/2017-03-25-18.grb2.html
#see top level TDS GUI at http://10.10.11.103:5000/thredds
import  requests
from lxml import etree
from io import StringIO
import re
from netCDF4 import Dataset
import numpy as np


base_url="http://10.10.11.103:5000/thredds/catalog/historical/2017-03/"
catalog="catalog.html"
base_url_files="http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/"

def get_file_list(url_folder):
    print("Getting files " + url_folder)
    resp_obj=requests.get(url_folder)
    cat_page=resp_obj.text.strip()
    file_entry_regex="<tt>(.+)</tt>"
    matches=re.findall(file_entry_regex,cat_page)
    file_list=list(filter(lambda x: "grb2" in x,matches))
    return file_list

    #html_parser=etree.HTMLParser()
    #tree=etree.parse(StringIO(cat_page),html_parser)
    # find all the tt elements


array_list=[]
file_list=get_file_list(base_url + catalog)
print(file_list)
for f in file_list:    
 url=base_url_files + f + "?time1[0],Temperature_surface[0][0:360][0:719]"
 #print(url)
 netcdf=Dataset(url)
 array_list.append( netcdf.variables['Temperature_surface'][:][:][:][0])
 #print(historical_data_of_interest.shape)

final_array=np.concatenate(array_list)

# compute avg temp as baseline
avg_temp = np.mean(final_array)
print(avg_temp)
