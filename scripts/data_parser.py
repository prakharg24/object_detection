import argparse
import numpy as np
import os

from utils import read_csv, read_json, write_csv, write_json, dump_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--inputs', type=str, required=True, help='All input data folders, seperated by comma')
	parser.add_argument('--output', type=str, required=True, help='Output folder for all the annotations')
	parser.add_argument('--split', type=float, default=0.8, help='Train split')
	
	args = parser.parse_args()

	train_data = []
	test_data = []
	fldr_arr = args.inputs.split(',')
	for fldr in fldr_arr:
		compl_data, header = read_csv(fldr + '/annotation.csv', column_header=True)
		write_json(fldr + '/annotation_coco.json', compl_data, fldr)
		
		json_data = read_json(fldr + '/annotation_coco.json')
		json_data = json_data['data']
		np.random.shuffle(json_data)


		train_split = int(args.split*len(json_data))
		train_data.extend(json_data[:train_split])
		test_data.extend(json_data[train_split:])


	np.random.shuffle(train_data)
	np.random.shuffle(test_data)

	train_dict = {}
	train_dict['data'] = train_data
	dump_json(args.output + '/train_coco.json', train_dict)

	test_dict = {}
	test_dict['data'] = test_data
	dump_json(args.output + '/test_coco.json', test_dict)
	
	write_csv(args.output + '/train_frcnn.txt', train_data)

	write_csv(args.output + '/test_frcnn.txt', test_data)

