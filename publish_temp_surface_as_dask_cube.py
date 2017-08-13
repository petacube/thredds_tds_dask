
from distributed import Client
from thredds_configuration import file_list_url,data_request, data_folder, thredds_servers, base_url
from dask_configuration import dask_scheduler_url
from thredds_utils import list_thredds_folder, compute_url_to_thredds_server_map, compute_avg_func
import xarray as xr



file_list=list_thredds_folder(file_list_url)



# connect to dask
client = Client(dask_scheduler_url)

url_list=[]
for f in file_list:    
 url_list.append(base_url + "/" + data_request + "/" + data_folder + "/" + f + "?time1[0],Temperature_surface[0][0:360][0:719]")

ds_temp_surface=xr.open_mfdataset(url_list)

ds_temp_surface.persist()
# this works because of https://github.com/dask/dask/blob/8c080b88c303cd64f41d7c7a7cde4f4f2faa10a9/dask/base.py#L569


# client persist does not currently - work in progress with dask team to fix!!
# see discussion at https://github.com/dask/dask/pull/1068
#client.persist(ds_temp_surface)
# this loads distributed cube into memory of dask workers

#ds_temp_surface.publish()
client.publish_dataset(temp_surface=ds_temp_surface)


# now this makes  distributed cube is available to all clients


