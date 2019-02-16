import argparse
import numpy as np
from utils import read_csv, write_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input csv folder')

	args = parser.parse_args()

	compl_data, header = read_csv(args.input + '/annotation.csv', column_header=True)

	write_json(args.input + '/annotation_coco.json', compl_data)