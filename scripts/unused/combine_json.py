import argparse
import numpy as np
from utils import read_json, dump_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--inputs', type=str, required=True, help='Input all json file, seperated by comma')
	parser.add_argument('--output', type=str, required=True, help='Output json file')

	args = parser.parse_args()

	file_arr = args.inputs.split(',')

	compl_data = []
	for ele in file_arr:
		curr_data = read_json(ele)
		compl_data.extend(curr_data['data'])

	final_dict = {}
	final_dict['data'] = compl_data
	dump_json(args.output, final_dict)