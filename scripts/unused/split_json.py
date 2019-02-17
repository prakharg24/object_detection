import argparse
import numpy as np
import json

from utils import read_json, dump_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input json file')
	parser.add_argument('--split', type=float, default=0.8, help='Train Split')
	parser.add_argument('--out_train', type=str, required=True, help='Train json file output')
	parser.add_argument('--out_test', type=str, required=True, help='Test json file output')

	args = parser.parse_args()

	json_data = read_json(args.input)
	compl_data = json_data['data']
	train_split = int(args.split*len(compl_data))
	np.random.shuffle(compl_data)


	train_data = {}
	train_data['data'] = compl_data[:train_split]
	dump_json(args.out_train, train_data)

	test_data = {}
	test_data['data'] = compl_data[train_split:]
	dump_json(args.out_test, test_data)