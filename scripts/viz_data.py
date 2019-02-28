import argparse
import cv2

from utils import read_json

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=str, required=True, help='Input json file')
	
	args = parser.parse_args()
	
	compl_data = read_json(args.input)
	compl_data = compl_data['data']

	for data in compl_data:

		img = cv2.imread(data['image_name'])
		for ele in data['annotations']:
			print(ele)
			cv2.rectangle(img,(int(ele['xmin']), int(ele['ymin'])), (int(ele['xmax']), int(ele['ymax'])), (0, 0, 0), 2)

			# textLabel = '{}: {}'.format(key,int(100*new_probs[jk]))

			# (retval,baseLine) = cv2.getTextSize(textLabel,cv2.FONT_HERSHEY_COMPLEX,1,1)
			# textOrg = (real_x1, real_y1-0)

			# cv2.rectangle(img, (textOrg[0] - 5, textOrg[1]+baseLine - 5), (textOrg[0]+retval[0] + 5, textOrg[1]-retval[1] - 5), (0, 0, 0), 2)
			# cv2.rectangle(img, (textOrg[0] - 5,textOrg[1]+baseLine - 5), (textOrg[0]+retval[0] + 5, textOrg[1]-retval[1] - 5), (255, 255, 255), -1)
			# cv2.putText(img, textLabel, textOrg, cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1)

		cv2.imshow('img', img)
		cv2.waitKey(0)
