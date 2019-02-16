import argparse
import numpy as np
import json

from utils import read_json, dump_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input json folder Location')
	parser.add_argument('--split', type=float, default=0.8, help='Train Split')

	args = parser.parse_args()

	json_data = read_json(args.input + '/annotation_coco.json')
	compl_data = json_data['data']
	train_split = int(args.split*len(compl_data))
	np.random.shuffle(compl_data)


	train_data = {}
	train_data['data'] = compl_data[:train_split]
	dump_json(args.input + '/train_coco.json', train_data)

	test_data = {}
	test_data['data'] = compl_data[train_split:]
	dump_json(args.input + '/test_coco.json', test_data)