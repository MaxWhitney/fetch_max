# Everything should have a test file, so this is the start of that.
import fetch_max
import logging

def main():
	# Configure the logging system
	logging.basicConfig(
		filename='test_fetch_max.log',
		filemode='w',
		level=logging.DEBUG
	)
	print("Hello fellow humans.")
	logging.info("I said hello to the humans.")

	# Setup up directories with hardcoded defaults
	fetch_max.setup_directories()

	# set up the datafile directories and tracking file
	df_dir = "some_bullshit"
	arch_dir = "archived_bullshit"
	tracking_suffix = "electric_fence"
	# setup directories with parameters
	fetch_max.setup_directories(df_dir, arch_dir)
	# setup directories with config file names
	prev_df_dir = df_dir
	df_dir = fetch_max.read_datafile_dir()
	arch_dir = fetch_max.read_archivefile_dir()
	fetch_max.setup_directories(df_dir, arch_dir)



	# Fetch with the hardcoded defaults, include an empty API key
	fetch_max.fetch_socrata_csv()

	# Fetch passing arguments in
	fetch_max.fetch_socrata_csv("yQJfX3SJA8E9KuFQEw7pubH2a", "data.ct.gov", "y6p2-px98") 

	# Fetch with config file settings, DEFAULT section
	token = fetch_max.read_socrata_token()
	domain = fetch_max.read_socrata_domain()
	data_id = fetch_max.read_socrata_id()
	fetch_max.fetch_socrata_csv(token, domain, data_id)

	# Fetch with config file setting from custom section
	token = fetch_max.read_socrata_token() # Always the same token
	domain = fetch_max.read_socrata_domain(section="nyc")
	data_id = fetch_max.read_socrata_id(section="nyc")
	fetch_max.fetch_socrata_csv(token, domain, data_id)	

	print("FRIENDLY HUMAN: Remember to clean up after yourself.")
	print("Think hard, then consider running 'rm -r datafiles'")
	print("Think hard, then consider running 'rm -r "+ prev_df_dir + "'")
	print("Think hard, then consider running 'rm -r "+ df_dir + "'")

if __name__ == "__main__":
	main()
