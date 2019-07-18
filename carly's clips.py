hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#soma de todos os preços
total_price = 0
for i in prices:
  total_price += i
print(total_price)

#média dos cortes de cabelo
average_price = total_price/len(prices)
print("Average Haircut Price: ", average_price)

#novos preços depois de retirar 5
new_prices = [x-5 for x in prices]
print(new_prices)

#soma de todo dinheiro ganhado
total_revenue = 0
for y in range(len(hairstyles)):
   total_revenue += prices[y] * last_week[y]
print("Total Revenue: ", total_revenue)

#ganho médio diário
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#cortes abaixo de 30 utilizando a nova lista de preços com condicional e index
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cortes abaixo de 30:", cuts_under_30)
