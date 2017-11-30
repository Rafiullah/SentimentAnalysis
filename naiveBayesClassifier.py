from textblob.classifiers import NaiveBayesClassifier

#experimenting with Dari
#put you training data to here .... to the train variable
train = [('استاد سیاف رمز عزت و سر افرازی ، امت اسلامی ، و تاج وقار ملت افغانستان است','pos'),
              ('شیطان بزرگ جهان خر سیاف', 'neg')]

#put your test data in here
test =  [('استاد سیاف رمز عزت و سر افرازی ، امت اسلامی ، و تاج وقار ملت افغانستان است','pos'),
              ('شیطان بزرگ جهان خر سیاف', 'neg')]


clf_dari = NaiveBayesClassifier(train)
print(clf_dari.classify("شیطان بزرگ"))
