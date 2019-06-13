import pandas as pd
from tqdm import tqdm
import numpy as np
import time
import os

def print_stories_as_txt(dataframe, fname):
	a = time.time()
	file = open(fname, "w")
	print("Reading stories to memory ...")
	for index, row in dataframe.iterrows():
		for col in dataframe.columns:
			file.write(row[col] + ' ')
		file.write('\n')
	print("Done in {} s".format(time.time() - a))
    
	file.close()

print("Loading Data...\n")

train = pd.read_csv('data/train_stories.csv')
val = pd.read_csv('data/cloze_test_val__spring2016 - cloze_test_ALL_val.csv')
test = pd.read_csv('data/cloze_test_test__spring2016 - cloze_test_ALL_test.csv')

final_test = pd.read_csv('data/test-stories.csv')

train = train.drop("storytitle", axis=1).drop("storyid", axis=1)

val = val.drop("InputStoryid", axis=1)
val_answer = val["AnswerRightEnding"]
val_sentences = val.drop("AnswerRightEnding", axis=1)

test = test.drop("InputStoryid", axis=1)
test_answer = test["AnswerRightEnding"]
test_sentences = test.drop("AnswerRightEnding", axis=1)

print_stories_as_txt(train, 'train_frame_model.txt')
print_stories_as_txt(val_sentences, 'train.txt')
print_stories_as_txt(test_sentences, 'val.txt')
print_stories_as_txt(final_test, 'test.txt')

np.savetxt('train_label.txt', val_answer)
np.savetxt('val_label.txt', test_answer)