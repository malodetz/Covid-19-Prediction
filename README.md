# Covid-19-Prediction

Building an autoregressive model to predict number of people with Covid-19.

Weights are calculated via least squares method by building and solving system of linear equations via Gaussian elimination.

Allows to explore variety of models for the same data, with different order and optional constant.

Most accurate results (much better than other models) were shown by model of order 13, which is an incubation period of Covid-19.
