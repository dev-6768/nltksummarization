# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:07:18 2022

@author: HP
"""

#import io, os
#input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

#from sys import stdin, stdout
#instead of "input()" use "stdin.readline().rstrip()"
#instead of "print()" use "stdout.write()"


# from PIL import Image
from flask import Flask, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
# from pytesseract import pytesseract


# path_to_tesseract = r"D:\Sanidhya_Mishra\Tesseract\tesseract.exe"
# image_path = r"E:\SampleVid\SampleHandwritingImage3.webp"
# img = Image.open(image_path)
# pytesseract.tesseract_cmd = path_to_tesseract
# imageToText = pytesseract.image_to_string(img)
# #print(imageToText[:-1])

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def summarization():
    
    text = str(request.args['query'])
    
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
    
    
    freqTable = dict()
    for word in words:
    	word = word.lower()
    	if word in stopWords:
    		continue
    	if word in freqTable:
    		freqTable[word] += 1
    	else:
    		freqTable[word] = 1
    
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    
    for sentence in sentences:
    	for word, freq in freqTable.items():
    		if word in sentence.lower():
    			if sentence in sentenceValue:
    				sentenceValue[sentence] += freq
    			else:
    				sentenceValue[sentence] = freq
    
    
    
    sumValues = 0
    for sentence in sentenceValue:
    	sumValues += sentenceValue[sentence]
    
    average = int(sumValues / len(sentenceValue))
    
    summary = ''
    for sentence in sentences:
    	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
    		summary += " " + sentence
            
    return {"output":summary}

#print(summarization())
if(__name__ == "__main__"):
    app.run()
    
    
    
    
