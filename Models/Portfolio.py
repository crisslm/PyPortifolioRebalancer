#CLIENT PORTFOLIO
class Portfolio:
    def __init__(self, owner):
        self.owner = owner
        self.assets = []

    def get_owner(self):
        return self.owner

    def add_asset(self, asset):
        self.assets.append(asset)

    def total_value(self):
        return sum(asset.total_asset_value() for asset in self.assets)

    def value_per_category(self, category):
        categorySum = 0
        for asset in self.assets:
            if asset.get_category() == category:
                categorySum += asset.total_asset_value()

        return categorySum

    def percentage_per_category(self, category):
        total = self.total_value()
        category_value = self.value_per_category(category)
        percentage = (category_value / total) * 100

        return percentage
