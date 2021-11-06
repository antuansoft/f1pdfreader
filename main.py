


from crawlf1web2021 import Crawlf1web2021


def main():
    print("main")

    bahrain2021 = Crawlf1web2021("https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/classification/9bb465b8-a1d7-4d67-beaf-c6b7a310d65a",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/drivers",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/standings/teams",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=PitStop",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=FastestLap",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapChart",
                                 "https://fiaresultsandstatistics.motorsportstats.com/results/2021-formula-1-gulf-air-bahrain-grand-prix/session-facts/b98847af-40d6-4464-9727-f638d1170fb0?fact=LapTime",
                                 "https://www.racefans.net/2021/03/29/2021-bahrain-grand-prix-interactive-data-lap-charts-times-and-tyres/"
                                 )
    bahrain2021.load()
if __name__ == "__main__":
    main()