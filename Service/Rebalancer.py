from Util.util import comparing_allocations_stocks, comparing_allocations_reits, comparing_allocations_bonds


class Rebalancer:
    def __init__(self, portfolio, allocation_strategy):
        self.portfolio = portfolio
        self.allocation_strategy = allocation_strategy

    def current_allocation(self):
        stocksValue = self.portfolio.percentage_per_category("stocks")
        reitsValue = self.portfolio.percentage_per_category("reits")
        bondsValue = self.portfolio.percentage_per_category("bonds")
        return [stocksValue, reitsValue, bondsValue]

    def comparing_allocations(self):
        currentAllocation = self.current_allocation()
        targetAllocation = self.allocation_strategy.target_allocation()
        return [comparing_allocations_stocks(currentAllocation[0], targetAllocation[0]),
                  comparing_allocations_reits(currentAllocation[1], targetAllocation[1]),
                  comparing_allocations_bonds(currentAllocation[2], targetAllocation[2])]

    def rebalance_sugestions(self):
        newWay = self.comparing_allocations()
        print(newWay[0])
        print(newWay[1])
        print(newWay[2])