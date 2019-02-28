import sys
import numpy as np
from utils import read_json, dump_json

def join_bbox(bbox1, bbox2):
	x1_t, y1_t, x2_t, y2_t = bbox1[0], bbox1[1], bbox1[2]+bbox1[0], bbox1[3]+bbox1[1]
	x1_p, y1_p, x2_p, y2_p = bbox2[0], bbox2[1], bbox2[2]+bbox2[0], bbox2[3]+bbox2[1]
	
	# x1_n = max(x1_t, x1_p)
	# y1_n = max(y1_t, y1_p)
	# x2_n = min(x2_t, x2_p)
	# y2_n = min(y2_t, y2_p)

	x1_n = min(x1_t, x1_p)
	y1_n = min(y1_t, y1_p)
	x2_n = max(x2_t, x2_p)
	y2_n = max(y2_t, y2_p)

	# x1_n = (x1_t + x1_p)//2
	# y1_n = (y1_t + y1_p)//2
	# x2_n = (x2_t + x2_p)//2
	# y2_n = (y2_t + y2_p)//2	

	return x1_n, y1_n, x2_n - x1_n, y2_n - y1_n

def match_bbox(bbox1, bbox2):
	x1_t, y1_t, x2_t, y2_t = bbox1[0], bbox1[1], bbox1[2]+bbox1[0], bbox1[3]+bbox1[1]
	x1_p, y1_p, x2_p, y2_p = bbox2[0], bbox2[1], bbox2[2]+bbox2[0], bbox2[3]+bbox2[1]
	
	if (x2_t < x1_p or x2_p < x1_t or y2_t < y1_p or y2_p < y1_t):
		return 0.0

	far_x = np.min([x2_t, x2_p])
	near_x = np.max([x1_t, x1_p])
	far_y = np.min([y2_t, y2_p])
	near_y = np.max([y1_t, y1_p])

	inter_area = (far_x - near_x + 1) * (far_y - near_y + 1)
	true_box_area = (x2_t - x1_t + 1) * (y2_t - y1_t + 1)
	pred_box_area = (x2_p - x1_p + 1) * (y2_p - y1_p + 1)
	iou = inter_area / (true_box_area + pred_box_area - inter_area)

	if(iou>0.85):
		return True
	else:
		return False

data1 = read_json(sys.argv[1])
data2 = read_json(sys.argv[2])

data1_dict = {}

for ele in data1:
	if(ele['image_id'] in data1_dict):
		data1_dict[ele['image_id']].append(ele)
	else:
		data1_dict[ele['image_id']] = [ele]

new_data = []

got_new = False
temp_data = {}

for ele in data2:
	if(ele['image_id'] in data1_dict):
		img = data1_dict[ele['image_id']]
		for ann in img:
			if(ann["category_id"]==ele['category_id']):
				if(match_bbox(ann["bbox"], ele["bbox"])):
					print("Hey")
					new_bbox = join_bbox(ann["bbox"], ele["bbox"])
					new_scr = max(ann["score"], ele["score"])
					temp_data = {}
					temp_data["image_id"] = ele["image_id"]
					temp_data["category_id"] = ele["category_id"]
					temp_data["bbox"] = new_bbox
					temp_data["score"] = new_scr
					got_new = True
					break
	if(got_new==False):
		new_data.append(ele)
	else:
		new_data.append(temp_data)
		temp_data = {}
		got_new = False

dump_json("result.json", new_data)