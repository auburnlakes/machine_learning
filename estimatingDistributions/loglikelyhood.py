def loglikelihood(posprob, negprob, X_test, Y_test):
    """
    loglikelihood(posprob, negprob, X_test, Y_test) returns loglikelihood of each point in X_test

    Input:
        posprob: conditional probabilities for the positive class (d)
        negprob: conditional probabilities for the negative class (d)
        X_test : features (nxd)
        Y_test : labels (-1 or +1) (n)

    Output:
        loglikelihood of each point in X_test (n)
    """
    # YOUR CODE HERE
    raise NotImplementedError()

    n, d = X_test.shape
    loglikelihood = np.zeros(n)
    positive = (Y_test == 1)
    negative = (Y_test == -1)

    loglikelihood[positive] = X_test[positive] @ np.log(posprob) + (1 - X_test[positive]) @ np.log(1 - posprob)
    loglikelihood[negative] = X_test[negative] @ np.log(negprob) + (1 - X_test[negative]) @ np.log(1 - negprob)

    return loglikelihood

# compute the loglikelihood of the training set
posprob, negprob = naivebayesPXY(X, Y)
loglikelihood(posprob, negprob, X, Y)