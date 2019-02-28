import sys
import json

with open(sys.argv[1], 'r') as fp:
	data = json.load(fp)

data = data['data']

new_data = []

for ele in data[:250]:
	if(ele["image_name"][19:22]=="dog"):
		img_id = int(ele["image_name"][33:-4]) + 10000
	else:
		img_id = int(ele["image_name"][33:-4])

	# print(ele)
	# exit()
	for ann_ele in ele["pred_anno"]:
		img_temp = {}
		img_temp["image_id"] = img_id
		if(ann_ele[4]=="dog"):
			img_temp["category_id"] = 1
		else:
			img_temp["category_id"] = 0
		# img_temp["bbox"] = [ann_ele[1], ann_ele[0], ann_ele[3] - ann_ele[1], ann_ele[2] - ann_ele[0]]
		img_temp["bbox"] = [ann_ele[0], ann_ele[1], ann_ele[2] - ann_ele[0], ann_ele[3] - ann_ele[1]]
		img_temp["score"] = ann_ele[5]/100
		new_data.append(img_temp)

with open('pred_output.json', 'w') as fp:
	json.dump(new_data, fp)