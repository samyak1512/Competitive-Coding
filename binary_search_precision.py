def binary_search(hi, lo):
    ans = 0
    while hi-lo>1e-2:#precision
      mid = (hi+lo)/2.0
      if checker(mid):
        ans = mid 
        lo = mid #keep in mind here we are not doing mid - 1
      else:
        hi = mid #keep in mind here we are not doing mid - 1
    return round(ans, 1)
