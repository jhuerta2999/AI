import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.posReview = 0
        self.negReview = 0
        self.allWords = 0
        self.negWords = {}
        self.posWords = {}
        self.dictionary = {}

    def train(self, file):
        for line in file:

            line = line.replace('\n', '')
            line = line.replace(',','')
            line = line.replace('?','')
            line = line.replace('!','')
            line = line.replace('.','')
            line = line.replace('\'','')
            line = line.replace(';','')
            line = line.lower()

            ratingText = line.split('|')
            rating = ratingText[0]
            review = ratingText[2]
            words = review.split(" ")

            #Adding all words to dictionary and tracking occurences
            for word in words:
                self.dictionaries(self.dictionary, word)

            #Incrementing pos words and pos reviews
            if rating == "5":
                self.posReview = self.posReview + 1

                #For all words add them or increase occurence in pos dictionary
                for word in words:
                    self.dictionaries(self.posWords, word)

            #Incrementing neg words and neg reviews
            else:
                self.negReview = self.negReview + 1

                #For all words add them or increase occurence in neg dictionary
                for word in words:
                    self.dictionaries(self.negWords, word)

        self.allWords = self.posReview + self.negReview 

    #Increase counts or add words to all dictioanries
    def dictionaries(self, dictionary, word):
        if word in dictionary:
            dictionary[word] = dictionary[word] + 1
        else:
            dictionary[word] = 1
        
    def classify(self, file):        
        totalPosWords = 0
        totalNegWords = 0

        #Get total of all pos/neg words
        for word in self.posWords:
            totalPosWords = totalPosWords + self.posWords[word]
        for word in self.negWords:
            totalNegWords = totalNegWords + self.negWords[word]

        classified = []
        
        for line in file:
            line = line.replace('\n', '')
            line = line.replace(',','')
            line = line.replace('?','')
            line = line.replace('!','')
            line = line.replace('.','')
            line = line.replace('\'','')
            line = line.replace(';','')
            line = line.lower()

            ratingText = line.split('|')
            review = ratingText[2]
            words = review.split(" ")

            #Probability of class
            posProb = float(self.posReview/self.allWords)
            negProb = float(self.posReview/self.allWords)

            #Checking each words occurence in the pos/neg dictioanries
            for word in words:
                #smooth words
                goodAcc = self.smoothing(self.posWords, word)                
                badAcc = self.smoothing(self.negWords, word)

                #Probability = P(good/bad class) + P(smoothed good/bad word / sum of all good/bad words and dictionary)
                posProb += math.log10(float(goodAcc/(totalPosWords + len(self.dictionary))))
                negProb += math.log10(float(badAcc/(totalNegWords + len(self.dictionary))))
            
            #Comparing probability to apply sentiment rating
            if(posProb > negProb):
                classified.append("5")
            else:
                classified.append("1")

        return classified

    #Check if word in Dict and return smoothed count
    def smoothing(self, dictionary, word):
        words = 0
        if word in dictionary.keys():
            words = dictionary[word] + 1
        
        return words + 1