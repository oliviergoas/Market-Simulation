import sys
import matplotlib.pyplot as plt
import numpy as np
from asset import Asset
from option import Option

def main():
    spot = 100
    rate = 0.02
    vol = 0.20
    maturity = 10
    strike = 110
    N = maturity * 10
    nb_samples = 1000

    print("The asset has a spot price of", spot, ", a rate of", rate, "and a volatility of", vol, ".")

    payoff_type = int(input("Choose an option:\n1. Buy option (ST - K)+\n2. Sell option (K - ST)+\n3. Path-dependent sell option (K - max(St) - ST)+\n> "))
    if payoff_type != 1 and payoff_type != 2 and payoff_type != 3:
        sys.exit("Wrong input")
    strike = float(input("Enter a strike value: "))
    print("The option on this asset has a strike of ", strike, " and expires in ", maturity, " days.")

    asset = Asset(spot, rate, vol, maturity)
    option = Option(strike, maturity, payoff_type)

    # x axis: uniform repartition of maturity/N between 0 and maturity
    x = np.linspace(0, asset.maturity, N)
    # y axis: asset value simulation
    path = asset.simul_asset(N)
    # y axis: intermediate option payoffs computation
    payoffs = option.compute_payoffs(path, N)
    # y axis: intermediate option prices computation
    prices = option.compute_prices(nb_samples, asset, N)
    
    print("Option price at maturity date:", prices[-1])

    # Plotting
    fig, (plt1, plt2, plt3) = plt.subplots(3)
    plt1.plot(x, path, "b", label="Asset")
    plt1.plot(x, np.repeat(strike, len(x)), "r", label="Strike")
    plt2.plot(x, payoffs, "b", label="Payoff")
    plt3.plot(x, prices, "b", label="Price")

    plt1.set_xlabel("Time")
    plt1.set_ylabel("Value")
    plt2.set_xlabel("Time")
    plt2.set_ylabel("Value")
    plt3.set_ylabel("Time")
    plt3.set_ylabel("Value")

    plt1.legend()
    plt2.legend()
    plt3.legend()
    plt.show()

    plt.savefig("simulation.svg")

main()
