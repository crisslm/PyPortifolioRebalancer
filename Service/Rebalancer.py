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
        result = []
        result.append("Sell Stocks" if currentAllocation[0] > targetAllocation[0] else "Buy Stocks")
        result.append("Sell REITs" if currentAllocation[1] > targetAllocation[1] else "Buy REITs")
        result.append("Sell Bonds" if currentAllocation[2] > targetAllocation[2] else "Buy Bonds")
        return result

    def rebalance_sugestions(self):
        newWay = self.comparing_allocations()
        print(newWay[0])
        print(newWay[1])
        print(newWay[2])