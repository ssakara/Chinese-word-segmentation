def main():
    import read_bakeoff2003
    import MakeDataSet
    import numpy
    import sklearn.linear_model as skl
	
    #Read in the Data
    train,errors = read_bakeoff2003.read_data(filepath='bakeoff2003/TrainingSinicaCorpus.txt')
    test,errors = read_bakeoff2003.read_data(filepath='bakeoff2003/as-testref.txt')
#Create the training and testing sets
    training = MakeDataSet.makeDataSet(train)
    testing = MakeDataSet.makeDataSet(test)

#Calculate the probabilities of occurence of the characters n-grams
    d = MakeDataSet.makeProbabilityDictionary(training)
    probs,depvar = MakeDataSet.makeProbabilityDataSet(training,d)
    dtest = MakeDataSet.makeProbabilityDictionary(testing)
    testProbs, testDepvar = MakeDataSet.makeProbabilityDataSet(testing,dtest)

#Run logistic regression classification
    features = numpy.array(probs)
    labels = numpy.array(depvar)
    testFeatures = numpy.array(testProbs)
    testLabels = numpy.array(testDepvar)
    logreg = skl.LogisticRegression()
	#train
    logreg.fit(features,labels)
	#test
    score = logreg.score(testFeatures, testLabels)
    return score
