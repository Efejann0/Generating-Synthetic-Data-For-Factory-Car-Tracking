import randomdatamatching as RandomDataMatching
import factorycircle as FactoryCircle


def main():
    fabrics_in_the_factory, yabbys = RandomDataMatching.t_zero_monent()
    FactoryCircle.simulation_function(fabrics_in_the_factory, yabbys)
if __name__ == "__main__":
    main()
