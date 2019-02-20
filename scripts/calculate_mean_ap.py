import numpy as np

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

def get_score(gt_bbox, pred_bbox):
	iou = []
	for i in range(10):
		iou.append(0.5 + i*0.05)

	tp, fp, fn = 0, 0

	iou_thres = 0.5

	for pred_ele in pred_bbox:
		found_match = False
		for gt_ele in gt_bbox:
			calc_iou = calculate_overlap(gt_ele, pred_ele)
			if(calc_iou > iou_thres):
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
			if(calc_iou > iou_thres):
				if(gt_ele['class']==pred_ele[4]):
					found_match = True
					break
		if(not found_match):
			fn += 1

	return tp, fp, fn