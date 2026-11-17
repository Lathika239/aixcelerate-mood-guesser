
# ==========================================
# AIXCELERATE - MOOD GUESSER
# LEVEL 1 + LEVEL 2 + TESTING
# ==========================================


# Training Dataset
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),

    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# ==========================================
# LEVEL 1: COUNT THE MOODS
# ==========================================

def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return (happy_count, sad_count)


print("LEVEL 1: COUNT THE MOODS")
print("Mood Count:", count_moods(train_data))


# ==========================================
# LEVEL 2: GUESS THE MOOD
# ==========================================

# Exactly 4 words in each list

happy_words = ["today", "won", "surprise", "tasty"]

sad_words = ["lost", "failed", "cancelled", "lonely"]


def guess_mood(sentence):

    clean_sentence = ""

    # Convert to lowercase and remove punctuation
    for char in sentence:
        if char.isalnum():
            clean_sentence += char.lower()
        else:
            clean_sentence += " "

    words = clean_sentence.split()

    happy_count = 0
    sad_count = 0

    # Count clue words
    for word in words:
        if word in happy_words:
            happy_count += 1

        if word in sad_words:
            sad_count += 1

    # Decide the mood
    if happy_count > sad_count:
        return "Happy"
    else:
        # Tie goes to Sad
        return "Sad"


# ==========================================
# SAMPLE TESTING
# ==========================================

print("\nLEVEL 2: SAMPLE TESTING")

test_sentences = [
    "We won the college match!",
    "I lost my phone",
    "The food was really tasty",
    "I failed the exam"
]

for sentence in test_sentences:
    print(sentence, "=", guess_mood(sentence))


# ==========================================
# TEST ALL 15 TRAINING SENTENCES
# ==========================================

print("\nTESTING ALL TRAINING DATA")

correct = 0

for sentence, actual_mood in train_data:

    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual:", actual_mood)
    print("Predicted:", predicted_mood)

    if actual_mood == predicted_mood:
        correct += 1

    print("----------------------------")


# ==========================================
# FINAL ACCURACY
# ==========================================

total = len(train_data)

accuracy = (correct / total) * 100

print("\nFINAL RESULTS")
print("Correct predictions:", correct, "/", total)
print("Accuracy:", round(accuracy, 2), "%")

# ==========================================
# LEVEL 3: PRACTICE TESTING
# ==========================================

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]

print("\nLEVEL 3: PRACTICE TESTING")

correct_level2 = 0

for sentence, actual_mood in practice_data:

    predicted = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual:", actual_mood)
    print("Predicted:", predicted)

    if predicted == actual_mood:
        correct_level2 += 1

accuracy_level2 = (
    correct_level2 / len(practice_data)
) * 100

print("\nLEVEL 2 ACCURACY:",
      round(accuracy_level2, 2), "%")


# ==========================================
# BONUS: LEARN WORD SCORES
# ==========================================

def learn_scores(data):

    word_scores = {}

    for sentence, mood in data:

        clean_sentence = ""

        for char in sentence:
            if char.isalnum():
                clean_sentence += char.lower()
            else:
                clean_sentence += " "

        words = clean_sentence.split()

        for word in words:

            if word not in word_scores:
                word_scores[word] = 0

            if mood == "Happy":
                word_scores[word] += 1

            elif mood == "Sad":
                word_scores[word] -= 1

    return word_scores


# Learn from training data
word_scores = learn_scores(train_data)


# ==========================================
# LEARNED MOOD GUESSER
# ==========================================

def guess_mood_learned(sentence):

    total_score = 0

    clean_sentence = ""

    for char in sentence:
        if char.isalnum():
            clean_sentence += char.lower()
        else:
            clean_sentence += " "

    words = clean_sentence.split()

    for word in words:
        total_score += word_scores.get(word, 0)

    if total_score > 0:
        return "Happy"
    else:
        return "Sad"


# ==========================================
# TEST LEARNED MODEL
# ==========================================

print("\nLEVEL 3: LEARNED MODEL")

correct_learned = 0

for sentence, actual_mood in practice_data:

    predicted = guess_mood_learned(sentence)

    print("\nSentence:", sentence)
    print("Actual:", actual_mood)
    print("Learned prediction:", predicted)

    if predicted == actual_mood:
        correct_learned += 1

accuracy_learned = (
    correct_learned / len(practice_data)
) * 100

print("\nLEARNED MODEL ACCURACY:",
      round(accuracy_learned, 2), "%")


# ==========================================
# FINAL COMPARISON
# ==========================================

print("\nFINAL COMPARISON")

print("Level 2 Accuracy:",
      round(accuracy_level2, 2), "%")

print("Learned Model Accuracy:",
      round(accuracy_learned, 2), "%")
