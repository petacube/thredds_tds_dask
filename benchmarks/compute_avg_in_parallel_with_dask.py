
import  requests
import re
from netCDF4 import Dataset
import numpy as np
# dask client
from distributed import Client
from os.path import join
from math import ceil
from thredds_configuration import file_list_url,data_request, data_folder, thredds_servers
from dask_configuration import dask_scheduler_url
from thredds_utils import list_thredds_folder, compute_url_to_thredds_server_map, compute_avg_func



array_list=[]
file_list=list_thredds_folder(file_list_url)



# connect to dask
client = Client(dask_scheduler_url)

url_list=[]
for f in file_list:    
 url_list.append(data_request + "/" + data_folder + "/" + f + "?time1[0],Temperature_surface[0][0:360][0:719]")


# allocate url to threads servers
server_url_mapping = compute_url_to_thredds_server_map(url_list,thredds_servers)

# launch the dask computation and collect results
avg_results_status = client.map(compute_avg_func,server_url_mapping)
avg_results=client.gather(avg_results_status)

final_avg=np.mean(avg_results)

print(final_avg)
