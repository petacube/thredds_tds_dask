
import  requests
import re
from netCDF4 import Dataset
import numpy as np
from math import ceil


def list_thredds_folder(url_folder):
    resp_obj=requests.get(url_folder)
    cat_page=resp_obj.text.strip()
    file_entry_regex="<tt>(.+)</tt>"
    matches=re.findall(file_entry_regex,cat_page)
    file_list=list(filter(lambda x: "grb2" in x,matches))
    return file_list

def compute_url_to_thredds_server_map(p_url_list, p_thredds_servers):
    num_urls = len(p_url_list)
    num_servers = len(p_thredds_servers)
    times_to_repeat = ceil((1.0 * num_urls) / (1.0 * num_servers))
    servers_repeated = thredds_servers * times_to_repeat
    # clamp to match number of urls
    servers_repeated = servers_repeated[:num_urls]
    # form the server url pair
    server_url_mapping = list(zip(p_thredds_servers, p_url_list))
    return server_url_mapping

def compute_avg_func(param,variable="Temperature_Surface"):
    # this function computes avg value of a variable
    # the first argument param is tuple of thredds server url
    # the second is file on the the thredds server
    thredds_server=param[0]
    file_url=param[1]
    full_file_url = thredds_server + "/" + file_url
    netcdf=Dataset(full_file_url)
    temp=netcdf.variables[variable][:][:][:][0]
    avg_temp = np.mean(temp)
    return avg_temp