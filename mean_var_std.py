import numpy as np


def calculate(list):

  if (len(list) == 9):

    #converting list into a 3X3 matrix
    list1 = np.array(list)
    lt = list1.reshape(3, 3)
    #findind out the Variance of the list given as a parameter
    v1 = np.var(lt, axis=0).tolist()
    v2 = np.var(lt, axis=1).tolist()
    #calculating the flattened matrix which will be common for all
    fv = np.var(lt.flatten())
    #finding out the mean
    m1 = np.mean(lt, axis=0).tolist()
    m2 = np.mean(lt, axis=1).tolist()
    fm = np.mean(lt)
    #calculating the standard deviation
    sd1 = np.std(lt, axis=0).tolist()
    sd2 = np.std(lt, axis=1).tolist()
    fs = np.std(lt.flatten())

    #Finding min max and sum
    max1 = np.max(lt, axis=0).tolist()
    max2 = np.max(lt, axis=1).tolist()
    fmax = np.max(lt.flatten())
    min1 = np.min(lt, axis=0).tolist()
    min2 = np.min(lt, axis=1).tolist()
    fmin = np.min(lt.flatten())
    sum1 = np.sum(lt, axis=0).tolist()
    sum2 = np.sum(lt, axis=1).tolist()
    fsum = np.sum(lt.flatten())
    calculations = {
      'mean': [m1, m2, fm],
      'variance': [v1, v2, fv],
      'standard deviation': [sd1, sd2, fs],
      'max': [max1, max2, fmax],
      'min': [min1, min2, fmin],
      'sum': [sum1, sum2, fsum]
    }
  else:
    raise ValueError("List must contain nine numbers.")
  return calculations
