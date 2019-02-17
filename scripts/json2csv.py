import argparse
import numpy as np
from utils import read_json, write_csv

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input json file')
	parser.add_argument('--output', type=str, required=True, help='Output txt file')
	parser.add_argument('--proxy_add', type=str, default="", help='Proxy address before every image address')

	args = parser.parse_args()

	compl_data = read_json(args.input)

	data_arr = []
	for ele in compl_data['data']:
		for bbox in ele['annotations']:
			data_arr.append([args.proxy_add + ele['image_name'], bbox['xmin'], bbox['ymin'], bbox['xmax'], bbox['ymax'], bbox['class']])

	write_csv(args.output, data_arr)