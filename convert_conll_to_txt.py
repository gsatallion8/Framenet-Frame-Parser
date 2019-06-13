import time, os, sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--conll_file', help='input conll file path')
parser.add_argument('--out_file', help='output text file path')

args = parser.parse_args()

in_file = open(args.conll_file, 'r')

frames_list = []
frames = []
sentence_num = 0
for line in in_file.readlines():
	ele = line.split('\t')
	if ele == ['\n']:
		continue
	if sentence_num != int(ele[6]):
		frames_list.append(frames)
		frames = []
	if ele[13] != '_':
		frames.append(ele[13])

frames_list.append(frames)
in_file.close()

out_file = open(args.out_file, 'w')

for i in range(len(frames_list)):
	for j in range(len(frames_list[i])):
		out_file.write(frames_list[i][j] + '\t')
	out_file.write('\n')	

out_file.close()