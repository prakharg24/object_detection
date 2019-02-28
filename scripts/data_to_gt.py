import argparse
import numpy as np
import os

from utils import read_csv, read_json, write_csv, write_json, dump_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='All input data folders, seperated by comma')
	parser.add_argument('--output', type=str, required=True, help='Output folder for all the annotations')
	
	args = parser.parse_args()

	data = []
	fldr = args.input
	compl_data, header = read_csv(fldr + '/annotation.csv', column_header=True)
	write_json(fldr + '/annotation_coco.json', compl_data, fldr)