
# this sample data url which is served over opendap protocol supported by xarray dataset object
#url='http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/2017-03-25-18.grb2?Temperature_surface'
#navigated to GUI at http://10.10.11.103:5000/thredds/dodsC/historical/2017-03/2017-03-25-18.grb2.html
#see top level TDS GUI at http://10.10.11.103:5000/thredds

base_url="http://10.10.11.103:5000/thredds"
catalog_request="catalog/historical"
catalog_url="catalog.html"
data_request="dodsC/historical"
data_folder="2017-03"
variable_to_retrieve="Temperature_surface"

file_list_url=base_url + "/" + catalog_request + "/" + data_folder + "/" + catalog_url

# settings on cerbo network
thredds_servers=[
"http://10.10.11.103:5000/thredds",
"http://10.10.11.103:5001/thredds",
"http://10.10.11.103:5002/thredds",
"http://10.10.11.103:5003/thredds",
"http://10.10.11.103:5004/thredds"]

