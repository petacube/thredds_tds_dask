import xarray as xr
#url="http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/*.grb2"
#url="http://10.10.11.103:5000/thredds/catalog/historical/2017-03/catalog.html?dataset=historical_grib/2017-03/2017-03-25-06.grb2"                            
#url="http://10.10.11.103:5000/thredds/catalog/historical/2017-03/catalog.html?dataset=historical_grib/2017-03/2017-03-25-18.grb2"
#url="http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/2017-03-25-18.grb2.html"
#url="http://10.10.11.103:5000/thredds/fileServer/historical/2017-03/2017-03-25-18.grb2"
url='http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/2017-03-25-18.grb2?Temperature_surface'
#ds=xr.open_mfdataset(url,engine='pydap')
print(url)
ds=xr.open_dataset(url) 
print(ds)

ds2=xr.open_mfdataset([url])
print(ds2)
