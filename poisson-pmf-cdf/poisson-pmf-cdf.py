import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    dic = {}
    # pmf 
    pmf = (math.exp(-lam) * (lam ** k)) / math.factorial(k)

    # pmf = (f"{pmf:.6f}")

    # cdf 
    cdf = sum([(math.exp(-lam) * (lam ** i)) / math.factorial(i) for i in range(k + 1)])
    # cdf = (f"{cdf:.6f}")
    # add to dic
    dic["pmf"] = pmf
    dic["cdf"] = cdf
    return dic
    