import numpy as np
import argparse
from utils import read_json
import matplotlib.pyplot as plt

def calculate_overlap(gt_ele, pred_ele):
	x1_t, y1_t, x2_t, y2_t = int(gt_ele['xmin']), int(gt_ele['ymin']), int(gt_ele['xmax']), int(gt_ele['ymax'])
	x1_p, y1_p, x2_p, y2_p = pred_ele[0], pred_ele[1], pred_ele[2], pred_ele[3]
	
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
	return iou

def get_score(gt_bbox, pred_bbox_orig, iou_thres, conf_thr, img_width, img_height):

	imp_cls = ['cow', 'dog']

	pred_bbox = []
	for ele in pred_bbox_orig:
		if(ele[4] not in imp_cls):
			continue
		if(ele[5]/100>=conf_thr):
			pred_bbox.append([max(0, int(ele[0])), max(0, int(ele[1])), min(int(img_width), int(ele[2])), min(int(img_height), int(ele[3])), ele[4], ele[5]])
			# pred_bbox.append(ele)

	# print(len(pred_bbox_orig), len(pred_bbox))

	# print(gt_bbox, pred_bbox)

	tp, fp, fn = 0, 0, 0

	for pred_ele in pred_bbox:
		found_match = False
		for gt_ele in gt_bbox:
			calc_iou = calculate_overlap(gt_ele, pred_ele)
			if(calc_iou >= iou_thres):
				if(gt_ele['class']==pred_ele[4]):
					tp += 1
					found_match = True
					break
		if(not found_match):
			fp += 1

	for gt_ele in gt_bbox:
		found_match = False
		for pred_ele in pred_bbox:
			calc_iou = calculate_overlap(gt_ele, pred_ele)
			if(calc_iou >= iou_thres):
				if(gt_ele['class']==pred_ele[4]):
					found_match = True
					break
		if(not found_match):
			fn += 1

	return tp, fp, fn

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input_json', type=str, required=True, help='Input json file address')
	parser.add_argument('--pred_json', type=str, required=True, help='Pred json file address')
	
	args = parser.parse_args()

	gt_data = read_json(args.input_json)
	gt_data = gt_data['data']

	pred_data = read_json(args.pred_json)
	pred_data = pred_data['data']

	iou = []
	for i in range(10):
		iou.append(0.5 + i*0.05)
	avg_prec_arr = []

	thr_dict = {}

	for val in pred_data:
		for pred_info in val['pred_anno']:
			score = pred_info[5]/100
			if score not in thr_dict:
				thr_dict[score] = 1

	thr_dict = sorted(thr_dict.keys())

	pred_dict = {}
	for val in pred_data:
		pred_dict[val['image_name']] = val['pred_anno']

	for iou_thres in iou:
		prec = []
		recc = []

		for conf_thr in thr_dict:
			ttp, tfp, tfn = 0, 0, 0
			for ele in gt_data:
				tp, fp, fn = get_score(ele['annotations'], pred_dict[ele['image_name']], iou_thres, conf_thr, ele['width'], ele['height'])
				ttp += tp
				tfp += fp
				tfn += fn

			if((ttp+tfp)==0):
				pr = 0
			else:
				pr = ttp/(ttp + tfp)

			if((ttp + tfn)==0):
				re = 0
			else:
				re = ttp/(ttp + tfn)

			prec.append(pr)
			recc.append(re)

		precisions = np.array(prec)
		recalls = np.array(recc)
		# print(recalls)
		# plt.plot(recalls, precisions, 'ro')
		# plt.show()
		# plt.plot(thr_dict, precisions, 'ro')
		# plt.show()
		# plt.plot(thr_dict, recalls, 'ro')
		# plt.show()
		prec_at_rec = []
		for recall_level in np.linspace(0.0, 1.0, 11):
			try:
				args = np.argwhere(recalls >= recall_level).flatten()
				prec = max(precisions[args])
			except ValueError:
				prec = 0.0
			prec_at_rec.append(prec)
		avg_prec = np.mean(prec_at_rec)
		print(avg_prec)
		avg_prec_arr.append(avg_prec)

	print(avg_prec_arr)
	print(np.mean(avg_prec_arr))