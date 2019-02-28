import sys
import json

with open(sys.argv[1], 'r') as fp:
	data = json.load(fp)

data = data['data']

new_data = {}
new_data["categories"] = []

temp = {}
temp["id"] = 0
temp["name"] = "cow"
temp["supercategory"] = "cow"
new_data["categories"].append(temp)

temp = {}
temp["id"] = 1
temp["name"] = "dog"
temp["supercategory"] = "dog"
new_data["categories"].append(temp)

images_arr = []
annotations_arr = []

some_count = 0

for ele in data:
	img_temp = {}
	if(ele["image_name"][19:22]=="dog"):
		img_id = int(ele["image_name"][33:-4]) + 10000
	else:
		img_id = int(ele["image_name"][33:-4])
	img_temp["id"] = img_id
	img_temp["width"] = int(ele["width"])
	img_temp["height"] = int(ele["height"])
	images_arr.append(img_temp)

	for ann_ele in ele["annotations"]:
		ann_temp = {}
		ann_temp["id"] = some_count
		some_count += 1
		ann_temp["image_id"] = int(img_id)
		if(ann_ele["class"]=="dog"):
			ann_temp["category_id"] = 1
		else:
			ann_temp["category_id"] = 0
		ann_temp["bbox"] = [int(ann_ele["xmin"]), int(ann_ele["ymin"]), int(ann_ele["xmax"]) - int(ann_ele["xmin"]), int(ann_ele["ymax"]) - int(ann_ele["ymin"])]
		ann_temp["iscrowd"] = 0
		ann_temp["area"] = ann_temp["bbox"][2]*ann_temp["bbox"][3]
		annotations_arr.append(ann_temp)

new_data["images"] = images_arr
new_data["annotations"] = annotations_arr

with open('gt_output_yolo.json', 'w') as fp:
	json.dump(new_data, fp)