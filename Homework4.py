from collections import Counter

computer = {"computer", "programming", "language"}
medicine = {"disease", "cancer", "medicine", "doctor"}
food = {"food", "prepare", "cook"}
science = {"research","science","learn"}
machine = {"machine", "engineer", "design"}

textFiles = ["unlabeled-1.txt", "unlabeled-2.txt", "unlabeled-3.txt","unlabeled-4.txt","unlabeled-5.txt",
	"labeled-1.txt", "labeled-2.txt"]
	
wordBank = [computer, medicine,food,science,machine]

fileRead = open("unlabeled-1.txt", "r")
text = fileRead.read()
formatedText = Counter(text.split())

wordCount = 0
subjectNum = 0


for file in textFiles:
	scoreList = []
	fileRead = open(file, "r")
	text = fileRead.read()
	formatedText = Counter(text.split())
	for subject in wordBank:
		for word in subject:
			if word in formatedText:
				wordCount = text.count(word)
				subjectNum = subjectNum + wordCount
		wordCount = 0	
		scoreList.append(subjectNum)
		subjectNum = 0
	min = 0
	noneGreater = True
	for score in scoreList:
		if score > min:
			min = score
			noneGreater = False;

	topScore = scoreList.index(min)
	decidedSubject = ""
	if noneGreater == False:
		if topScore == 0:
			decidedSubject = "computers"	
		elif topScore == 1:
			decidedSubject = "medicine"
		elif topScore == 2:
			decidedSubject = "food"
		elif topScore == 3:
			decidedSubject = "science"
		elif topScore == 4:
			decidedSubject = "machine"
	else:
		decidedSubject = "Unknown Subject"	
	info = "Subject for: " + file + ": " + decidedSubject
	print(info)
			
