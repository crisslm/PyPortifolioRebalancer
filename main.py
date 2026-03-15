from Models.Asset import Asset
from Models.Portfolio import Portfolio
from Service.Rebalancer import Rebalancer
from Strategies.AllocationStrategy import AllocationStrategy

print("PORTFOLIO REBALANCE \n")

client1 = Portfolio("Cristian")
asset1 = Asset("RTN18", "stocks", 1500, 20)
asset2 = Asset("NAYS1", "reits", 698, 30)
asset3 = Asset("JKS1A", "bonds", 1239, 70)
client1.add_asset(asset1)
client1.add_asset(asset2)
client1.add_asset(asset3)

allocationStrategie = AllocationStrategy(60,25,15)
clientRebalance = Rebalancer(client1, allocationStrategie)

print("Portfolio from {}:\n".format(client1.get_owner()))
print("Total portfolio value: ${:.2f}\n".format(client1.total_value()))

print("Current Allocation:\n")
clientAllocation = clientRebalance.current_allocation()
print("Stocks: {:.2f}%".format(clientAllocation[0]))
print("REITs: {:.2f}%".format(clientAllocation[1]))
print("Bonds: {:.2f}%".format(clientAllocation[2]),"\n")

print("Target allocation: \n")
targetAllocation = allocationStrategie.target_allocation()
print("Stocks: {:.2f}%".format(targetAllocation[0]))
print("REITs: {:.2f}%".format(targetAllocation[1]))
print("Bonds: {:.2f}%".format(targetAllocation[2]),"\n")

print("System sugestion: ")
clientRebalance.rebalance_sugestions()