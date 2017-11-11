from sklearn.svm import LinearSVC
import pickle

#returns a linear SVM classifier
#see default values used for the model at
#http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
def get_classifier():
    return LinearSVC(random_state=int)

#trains the given classifier with the provided data
def train_clf(clf, feature_values, original_labels):
    clf.fit(feature_values, original_labels)


#takes a classifier, the data; returns the guessed labels
def classify(clf, feature_values):
    return clf.predict(feature_values)

#returns a string that can be used with SVM.get_classffier_object(s)
#to reconstruct the same object from the string
#the string can be stored on disk and the training won't be lost
def get_classifier_string(clf):
    return pickle.dumps(clf)

#returns an object from the saved classfier string
def get_classffier_object(string):
    return pickle.loads(string)