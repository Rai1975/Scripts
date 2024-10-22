import math
import scipy.stats as stats
import numpy as np
def variance(arr):
    sqr_arr = []

    for i in arr:
        sqr_arr.append(i**2)
    
    sumArr = sum(arr)
    sumSqArr = sum(sqr_arr)
    n = len(arr)

    numerator = sumSqArr - ((sumArr**2)/(n))
    denominator = n - 1

    return (numerator/denominator)

def perms(n,k):
    numerator = math.factorial(n)
    denominator = math.factorial(n-k)
    kf = math.factorial(k)

    return numerator/(denominator*kf)

def binomial_distribution(n,x,p):
    q = 1 - p   
    per = perms(n, x)

    return (per*(p**x)*(q**(n-x)))

# E(x)
def E(x, px):
    sum = 0
    for i in range(len(x)):
        sum += x[i]*px[i]
    
    return sum

# V(x)
def V(x, E, px):
    sum = 0
    for i in range(len(x)):
        sum += ((x[i] - E)**2)*px[i]
    
    return sum


def bino(s, n, p):
    perm = perms(n,s)
    res = perm * (p**(s)) * ((1-p)**(n-s))

    return res

def hyperGeometric(s, n, M, N):
    num1 = perms(M,s)
    num2 = perms(N-M, n-s)
    den = perms(N,n)

    return (num1*num2)/den

def poissonProb(mu, x):
    return stats.poisson.pmf(x, mu)

def normalProb(x, mean, std_dev):
    z = (x - mean)/std_dev
    pdf_value = stats.norm.cdf(z)

    return pdf_value

def func(n, p):
    one = (1-p)**n

    return one * p 

def logNormalProb(z, mu, sigma):
    return stats.norm.cdf(z, mu, sigma)


def pdfStandardBetaDistribution(x, alpha, beta):
    return((x**(alpha-1))*((1-x)**(beta-1)))