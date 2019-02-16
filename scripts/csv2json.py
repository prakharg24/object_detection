import argparse
import numpy as np
from utils import read_csv, write_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input csv file name')
	parser.add_argument('--output', type=str, required=True, help='Output json file name')

	args = parser.parse_args()

	compl_data, header = read_csv(args.input, column_header=True)

	write_json(args.output, compl_data)