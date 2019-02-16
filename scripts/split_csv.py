import argparse
import numpy as np
from utils import read_csv, write_csv

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Complete data folder')
	parser.add_argument('--split', type=float, default=0.8, help='Train Split')

	args = parser.parse_args()

	compl_data, header = read_csv(args.input + '/annotation.csv', column_header=True)
	train_split = int(args.split*len(compl_data))
	np.random.shuffle(compl_data)

	write_csv(args.input + '/train_ann.csv', compl_data[:train_split], column_header=header)
	write_csv(args.input + '/test_ann.csv', compl_data[train_split:], column_header=header)