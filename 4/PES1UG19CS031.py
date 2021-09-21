import numpy as np

class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        print("data", self.data, "target", self.target)

        return self

    def find_distance(self, x):
        """

        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        # TODO

        # x is given dataset
        dList = []
        for eachinput in x:
            d = []
            for eachtrial in self.data:
                d1 = (abs(eachtrial - eachinput))**(self.p)
                d.append((sum(d1))**(1/self.p))
            dList.append(d)   
        # print(dList, "is dList")  

        return dList

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        # TODO

        dists = self.find_distance(x)
        # print(">>>>distances")
        # for e in dists:
        #     print(e)

        result = [[], []]
        
        for idx in range(len(dists)):
            # print("------------\nin iteration i", idx)

            rownum = [j for j in range(len(self.data))]
            sorted_dists = sorted(zip(dists[idx], rownum))

            # print("!!!!!!!!!!!!!!!TEST1", sorted_dists)
            neigh_d = list(zip(*list(sorted_dists)))[0]
            neigh_idx = list(zip(*list(sorted_dists)))[1]

            result[0].append(neigh_d[0:self.k_neigh])
            result[1].append(neigh_idx[0:self.k_neigh])
            # print("RESULTS", result)
        # print("final asnwer = \n", result)
        return result

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        kneigh = self.k_neighbours(x)
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~\n{x}\n~~~~~~~~~~~~~~~~~~~~~~~~~\n{kneigh}~~~~~~~~~~~~~~~~~~~~~~")

        nearest = kneigh[0]
        indexes = kneigh[1]

        prediction = [0]*(len(nearest))
        print("prediction", prediction)

        for row in range(len(nearest)):
            

            print("$$$$$ ROW", row)
            for i in range(len(nearest)):
                print("-------\n", i)
                print("!!!!1", nearest[i], indexes[i])
                votes = { key:0 for key in np.unique(self.target)}
                print("VOTES", votes)
                for j in range(len(nearest[i])):
                    print(nearest[i][j], indexes[i][j], "%%")

                    if self.weighted == True:
                        # weighted
                        closeneigh = indexes[i][j]
                        weight = nearest[i][j] + 0.00000000001
                        votes[self.target[closeneigh]] += (1/weight)


                    if self.weighted == False:
                        # not weighted 
                        #  add up votes
                        closeneigh = indexes[i][j]
                        votes[self.target[closeneigh]] +=1
                        # pass
                print("VOTES for i=", row, votes)
                prediction[row] = max(zip(votes.values(), votes.keys()))[1]
                print(prediction, "is predicted class$$$$$$$$$$$$$$$$$$$")

        print(prediction)
        return prediction


        # [
        #   [(0.6124069400000001, 0.70111576, 0.7957107400000001),
        #   (0.7151229399999999, 0.9783993200000001, 1.2414143899999999),
        #   (0.64586644, 0.6784257499999999, 0.7519419199999999),
        #    (0.56278538, 0.8848947200000001, 1.00406933), 
        #    (0.4384014299999999, 0.44120603, 0.8628504700000001)]

        #    , [(2, 4, 9),
        #     (2, 4, 8), 
        #     (6, 9, 3),
        #      (3, 6, 9),
        #       (0, 4, 2)]
        # ]

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        # TODO

        prediction = self.predict(x)
        correct = np.sum(prediction == y)
        accuracy = ((correct/len(y))*100)
        
        return accuracy
        