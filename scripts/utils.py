import csv

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