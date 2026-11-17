# AIXcelerate – Mood Guesser

## Project Overview
A Python project developed for the AIXcelerate challenge to classify sentences as Happy or Sad.

## Level 1: Count the Moods
The program counts Happy and Sad sentences using a Python function.

Output: (8, 7)

## Level 2: Guess the Mood
The program uses four Happy clue words and four Sad clue words to predict the mood of a sentence.

Training accuracy: 80%

## Level 3: Testing
Accuracy on the 5 practice sentences: 100%

1. Which sentence went wrong (or was closest to going wrong), and why?

My program classified all five practice sentences correctly. The sentence "Today was a great day" was closest to going wrong because the program had not learned every word in that sentence.

2. One change that would make my program better:

I could improve the clue words and handle negation, such as "not good".

## Learning Questions

1. Total score of "good party today" and its mood: +3, Happy.
2. Total score of "bad exam day" and its mood: -3, Sad.
3. Why did "exam" get a score of 0, and is that good or bad?

It appears in both Happy and Sad examples, so its scores cancel. This is useful because it is not a strong clue for either mood.

4. Why is "not good" labelled Happy by this method, and how could it be fixed?

The method sees the positive score of "good" but does not understand the negative meaning of "not". It could be improved by checking negation words.

## AI Declaration

I used an AI tool: Yes.

If yes, what I asked it:

I used ChatGPT to understand Python functions, debug my code, improve my mood prediction program and learn how to test and publish my project on GitHub.

## Reflection

The hardest part was selecting clue words and improving the accuracy of my program. I learned how to count moods, classify sentences, calculate accuracy and build a simple word-score learning model using Python.
