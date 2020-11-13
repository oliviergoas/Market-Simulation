import math
from asset import Asset

class Option:
    def __init__(self, strike, maturity, payoff_type):
        self.strike = strike
        self.maturity = maturity
        self.payoff_type = payoff_type

    def compute_payoff(self, path):
        if self.payoff_type == 1:
            payoff = path[-1] - self.strike
        elif self.payoff_type == 2:
            payoff = self.strike - path[-1]
        elif self.payoff_type == 3:
            payoff = self.strike * max(path) - path[-1]
        else:
            return 0
        return payoff if payoff > 0 else 0

    def compute_payoffs(self, path, N):
        payoffs = []
        for i in range(N):
            sub_path = path[0:i+1]
            payoffs.append(self.compute_payoff(sub_path))
        return payoffs

    # The price equals the actualized payoff
    def compute_price(self, nb_samples, asset, N):
        sum = 0
        for i in range(nb_samples):
            path = asset.simul_asset(N)
            payoff = self.compute_payoff(path)
            sum += payoff
        return math.exp(-asset.rate * asset.maturity) * sum / nb_samples

    def compute_prices(self, nb_samples, asset, J):
        prices = [0]
        for i in range(1, J):
            prices.append(self.compute_price(nb_samples, asset, i))
        return prices
