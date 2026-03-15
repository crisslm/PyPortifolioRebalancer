class AllocationStrategy:
    def __init__(self, stocks, reits, bonds):
        self.stocks = stocks
        self.reits = reits
        self.bonds = bonds

    def target_allocation(self):
        return [self.stocks, self.reits, self.bonds]