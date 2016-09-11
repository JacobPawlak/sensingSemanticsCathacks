# sensingsemantics

Abstract

Sensing Semantics is a sentiment analysis engine. It takes in a file containing song lyrics, a short story, a poem, or indeed any form of written word, and analyzes the probability of each line being positive or negative by analyzing how many positive or negative words are contained in the line. Words like "happy", "joyful", and "puppy" are rated positive and words such as "anger", "hate", and "sad" are considered negative. It then produces a corralative sound and light of this probability. 

The program works by separating an input file by line, and then further separates these lines by sentances (splitting by periods). It then utilizes the SentiWordNet corpus of the Natural Language Tool Kit (NLTK) to determine the positive and negative values of each word in the line (assuming it has a positive or negative score between 0 and 1). It then uses the combined word scores to determine if the line is positive or negative.

After determining whether the line is positive or negative, the program determines a new positive/negative score on a 0-16 scale and plays a musical note for each line. The possible notes are the middle 32 notes on a piano, with the lower 16 being negative and the upper 16 being positive.

Additionally, Python scripts were made to generate arduino code for powering a 4x4x4 charlieplexed LED cube for extra visualization. Each layer of the cube was a different color and represented different values from our data, for instance the red layer displayed the line-negative score (0-16) where 0 lights meant the line had a raw negative score of 0, 16 lights was a raw negative score of 1.

The overall goal of this project was to provide a seperate visualization of semantic values from text data in an easy to understand manner. 
