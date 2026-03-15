from unicodedata import category

from Models.Asset import Asset
from Models.Portfolio import Portfolio
from Service.Rebalancer import Rebalancer
from Strategies.AllocationStrategy import AllocationStrategy
from Util.util import category_input, valid_input_assets

print("PORTFOLIO REBALANCE REPORT\n")

cliente_name = input("Client name: ")
client1 = Portfolio(cliente_name)

num = valid_input_assets()
for i in range(num):
    print("\nAsset [{}]: ".format(i+1))
    ticket = input("Ticket: ")
    category = category_input()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    asset = Asset(ticket,category,price,quantity)
    client1.add_asset(asset)

print("\nAllocation strategy: ")
stocks = int(input("Stocks: "))
reits = int(input("REITs: "))
bonds = int(input("Bonds: "))

allocationStrategy = AllocationStrategy(stocks, reits, bonds)
clientRebalance = Rebalancer(client1, allocationStrategy)

print("\n===========================")
print("Portfolio from {}:\n".format(client1.get_owner()))
print("Total portfolio value: ${:.2f}\n".format(client1.total_value()))

print("Current Allocation:\n")
clientAllocation = clientRebalance.current_allocation()
print("Stocks: {:.2f}%".format(clientAllocation[0]))
print("REITs: {:.2f}%".format(clientAllocation[1]))
print("Bonds: {:.2f}%".format(clientAllocation[2]),"\n")

print("Target allocation: \n")
targetAllocation = allocationStrategy.target_allocation()
print("Stocks: {:.2f}%".format(targetAllocation[0]))
print("REITs: {:.2f}%".format(targetAllocation[1]))
print("Bonds: {:.2f}%".format(targetAllocation[2]),"\n")

print("System sugestion: ")
clientRebalance.rebalance_sugestions()
print("===========================")