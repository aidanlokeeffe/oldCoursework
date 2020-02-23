def main():
  for i in range(1, 11):
    series = 0
    n = i * 10000
    while n > 0:
      series += ((-1) ** (n + 1)) / (2 * n - 1)
      n -= 1
    pi = 4 * series
    print(pi)
    
main()