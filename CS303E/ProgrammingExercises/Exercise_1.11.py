def main():
  # Define necessary values
  initial_population = 312032486

  seconds_per_year = 31536000

  change_births = seconds_per_year // 7
  change_deaths = seconds_per_year // 13
  change_immigration = seconds_per_year // 45

  net_change = change_births + change_immigration - change_deaths
  
  # Project populations
  pop_1 = initial_population + net_change
  pop_2 = initial_population + (2 * net_change)
  pop_3 = initial_population + (3 * net_change)
  pop_4 = initial_population + (4 * net_change)
  pop_5 = initial_population + (5 * net_change)

  # Print results
  print("The population values for the next five years are projected to be:")
  print(pop_1, pop_2, pop_3, pop_4, pop_5)

main()