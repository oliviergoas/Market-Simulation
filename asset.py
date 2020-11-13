import math
import simulation as sim

class Asset:
    def __init__(self, spot, rate, vol, maturity):
        self.spot = spot
        self.rate = rate
        self.vol = vol
        self.maturity = maturity

    # Simulates the variation of an asset's value over time
    def simul_asset(self, N):
        timestep = self.maturity/N
        # S0 = spot price
        asset = [self.spot]
        # St = S0 * exp((r - s*s/2)t + s*Wt)
        # Wt = √(ti+1 - ti) * X
        # X ~ N(0,1)
        for i in range(1, N):
            gaussian = sim.simul_gaussian(1)
            asset.append(asset[i-1] * math.exp((self.rate - self.vol**2 / 2) * timestep + self.vol * math.sqrt(timestep) * gaussian[0]))
        return asset
