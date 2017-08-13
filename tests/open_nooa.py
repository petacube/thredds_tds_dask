import xarray as xr
from datetime import datetime
dt = datetime(2016, 4, 16, 18)
url='https://nomads.ncdc.noaa.gov/thredds/dodsC/namanl/{0:%Y%m}/{0:%Y%m%d}/namanl_218_{0:%Y%m%d}_{0:%H}00_000.grb'.format(dt)
data = xr.open_dataset(url,decode_times=True)
print(data)
