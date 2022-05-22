#helper file to move data from specific locations and to generate corresponding annotations
import os
import shutil
from tqdm import tqdm
import numpy
import random

val_dataset_path = '../../datasets/gym99/event_frames_val_2_video_0.5_second_overlapping'
print(len(os.listdir(val_dataset_path)))

result = []
existing_videos_set = set()
count = 0
category_dict = {}
with open('train_set_frames.txt') as f:
	lines = f.readlines()
	for line in lines:
		count+=1
		if line[-3:-1] == '14':
			line = line[:-3]+'1'
			result.append(line)
			continue
		if int(line.split(' ')[-1][:-1]) in category_dict:
			if int(line.split(' ')[-1][:-1]) <= 9:
				category_dict[int(line.split(' ')[-1][:-1])].append(line[:-1])
			else:
				category_dict[int(line.split(' ')[-1][:-1])].append(line[:-1])
		else:
			if int(line.split(' ')[-1][:-1]) <= 9:
				category_dict[int(line.split(' ')[-1][:-1])] = [line[:-1]]
			else:
				category_dict[int(line.split(' ')[-1][:-1])] = [line[:-1]]
print(len(result))
for key in category_dict.keys():
	print(key, len(category_dict[key]))
	result = result + random.sample(category_dict[key],4)
#print(result)
print(result)


result = []
for video in tqdm(os.listdir(val_dataset_path)):
	if len(os.listdir(os.path.join(val_dataset_path,video))) == 0:
		os.rmdir(os.path.join(val_dataset_path,video))
		continue
	line = 'datasets/gym99/event_frames_val_2_video_0.5_second_overlapping/'+str(video)+' '+ str(len(os.listdir(os.path.join(val_dataset_path,video)))// 3) +' 14'
	result.append(line)

print(len(os.listdir(val_dataset_path)))
a_file = open("val_set_frames_2_video_detection_0.5_second_overlapping.txt", "w")
numpy.savetxt("val_set_frames_2_video_detection_0.5_second_overlapping.txt", result, delimiter=" ", newline = "\n", fmt="%s")
a_file.close()

val_video_path = '../../datasets/gym99/event_frames_val/A0xAXXysHUo_E_003089_003189'
target_path = '../../datasets/gym99/event_frames_val_2_video_0.5_second_overlapping'
for frame in tqdm(os.listdir(val_video_path)):
	for offset in range(15):
		start = int(frame[:-4])
		end = start+14
		folder_name = 'A0xAXXysHUo_E_003089_003189_A_'+str(start).zfill(5)+'_'+str(end).zfill(5)
		if not os.path.exists(os.path.join(target_path,folder_name)):
			os.mkdir(os.path.join(target_path,folder_name))
		shutil.copyfile(os.path.join(val_video_path,str(int(frame[:-4])+offset).zfill(5))+'.png',os.path.join(target_path,folder_name,str(offset).zfill(5)+'.png'))
