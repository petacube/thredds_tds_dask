

from distributed import Client
from dask_configuration import dask_scheduler_url


# connect to dask
client = Client(dask_scheduler_url)
temp_cube=client.get_dataset('temp_surface')
mean_temp=temp_cube.mean()
print(mean_temp)








