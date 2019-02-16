import csv
import json

def read_csv(file_addr, column_header=False):
	
	header = []
	data = []
	with open(file_addr) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				if(column_header):
					header = row
				else:
					data.append(row)
				line_count += 1
			else:
				data.append(row)
				line_count += 1

	return data, header

def write_csv(file_addr, data, column_header=None):
	
	with open(file_addr, mode='w', newline='') as employee_file:
		employee_writer = csv.writer(employee_file, delimiter=',')
		if(column_header):
			employee_writer.writerow(column_header)
	
		for ele in data:
			employee_writer.writerow(ele)

def write_json(file_addr, data):
	out_dict = {}
	image_dict = {}
	iter_img = 0

	out_dict['data'] = []
	for ele in data:
		temp_ann = {}
		temp_ann['class'] = ele[3]
		temp_ann['xmin'] = ele[4]
		temp_ann['ymin'] = ele[5]
		temp_ann['xmax'] = ele[6]
		temp_ann['ymax'] = ele[7]

		if(ele[0] in image_dict):
			curr_iter = image_dict[ele[0]]
		else:
			temp_img = {}
			image_dict[ele[0]] = iter_img
			temp_img['image_id'] = iter_img
			temp_img['image_name'] = ele[0]
			temp_img['width'] = ele[1]
			temp_img['height'] = ele[2]
			temp_img['annotations'] = []
			out_dict['data'].append(temp_img)
			curr_iter = iter_img
			iter_img += 1

		out_dict['data'][curr_iter]['annotations'].append(temp_ann)


	with open(file_addr, 'w') as fp:
		json.dump(out_dict, fp)