# SciCoder Task 2 - randsample
# You tell me how many things you want to sample and where you want to sample them from,
# and I'll give you that many unique random strings from that file to read.
# Created by Benjamin Metha
# Last updated: November 19 2018.

import random

def random_samples(n_samples = 10, filename="Datafiles/sdss_spectra_links.txt"):
	file_reader = open(filename)
	sample_indices = set()
	unique_strings = set()
	for line in file_reader:
	     unique_strings.add(line)
	file_reader.close()
	total_n_objects = len(unique_strings)
	while len(sample_indices) < n_samples:
		sample_indices.add(random.randint(0, total_n_objects))
		
	unique_strings = list(unique_strings)
	return [unique_strings[x] for x in sample_indices]
	
ten_randies = random_samples(n_samples = 10)
print(*ten_randies)