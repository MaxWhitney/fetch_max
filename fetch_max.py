# Utilities for fetching a Socrata data set
# depends on sodapy.py among other things ...

from sodapy import Socrata
import configparser
import os
import logging

SOCRATA_API_CONFIG_FILE="Socrata_API.cfg"

# This API Key is mah real key, don't go spreading it around
#SOCRATA_API_KEY="yQJfX3SJA8E9KuFQEw7pubH2a"
# Turns out you can send sodapy an empty key and it still retrieves data :)
SOCRATA_API_KEY=""

# Test domain and id for when you don't feed it any configuration at all
SOCRATA_DOMAIN="data.ct.gov"
SOCRATA_ID="y6p2-px98"
# together these resolve to https://data.ct.gov/resource/y6p2-px98.csv

# Intelligent defaults for directories & tracking
DF_DIR="datafiles"
ARCH_DIR="archived_datafiles"
TRACKING=".log"

#initializing logging -- do this properly as a class later
logging.basicConfig(
	filename='test_fetch_max.log',
	filemode='w',
	level=logging.DEBUG
)
print("Hello fellow humans, say I the fetch_socrata file.")
logging.info("I, fetch_socrata, said hello to the humans.")

# load up the config file reader
config = configparser.ConfigParser()
config.read(SOCRATA_API_CONFIG_FILE)

def fetch_socrata_csv(socrata_token=SOCRATA_API_KEY, 
			socrata_domain=SOCRATA_DOMAIN,
			socrata_id=SOCRATA_ID):
	## will need to add some logic around when to load the file but
	## working data connection code from here on
	print("Obtaining client with ", socrata_token, socrata_domain, socrata_id)
	client = Socrata(socrata_domain, socrata_token)
	select_count = client.get(socrata_id, content_type="csv",
				select="count(*)")
	print("type = ", type(select_count), " select_count = ", select_count)

##PSEUDO CODE FOR FILE RETRIEVAL PROCESS
# If not associated file exists
# Retrieve the data, store to a file, and drop some record keeping data
# version 2 will add retrieval of metadata, maybe.
# If an associated data file already exists
# 	Create a checksum of the file on disk
# 	Retrieve new data into a new file
# 	Checksum the new file
# 	If the checksums match, drop some record keeping data and delete new
#	Else archive existing and shift in the new file
# Confirm correctness by creating a DataPandas data frame from the file


def read_socrata_token(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
	socrata_api_key = config[section]['socratatoken']
	logging.debug("Read from config SocrataToken = %s", socrata_api_key)	
	return socrata_api_key

def read_socrata_domain(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
        socrata_domain = config[section]['socratadomain']
        logging.debug("Read from config SocrataDomain = %s", socrata_domain)
        return socrata_domain

def read_socrata_id(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
        socrata_id = config[section]['socrataid']
        logging.debug("Read from config SocrataId = %s", socrata_id)
        return socrata_id

def read_datafile_dir(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
        df_dir = config[section]['datafiledirectory']
        logging.debug("Read from config DataFileDirectory = %s", df_dir)
        return df_dir

def read_archivefile_dir(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
        arch_dir = config[section]['datafilearchive']
        logging.debug("Read from config DataFileArchive = %s", arch_dir)
        return arch_dir

def read_tracking_suffix(filename:str=SOCRATA_API_CONFIG_FILE, section:str="DEFAULT") -> str:
        tracking = config[section]['trackingsuffix']
        logging.debug("Read from config TrackingSuffix = %s", tracking)
        return tracking

def setup_directories(df_dir=DF_DIR, arch_dir=ARCH_DIR):
	if not os.path.isdir(df_dir):
		os.makedirs(df_dir)
	arch = os.path.join(df_dir, arch_dir)
	if not os.path.isdir(arch):
		os.makedirs(arch)
