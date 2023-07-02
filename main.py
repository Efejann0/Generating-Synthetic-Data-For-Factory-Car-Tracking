import randomdatamatching as RandomDataMatching
import factorycircle as FactoryCircle
import databasesave as dbsave


def main():
    fabrics_in_the_factory, yabbys = RandomDataMatching.t_zero_monent()
    while(True):
        fabrics_in_the_factory, yabbys = FactoryCircle.simulation_function(fabrics_in_the_factory, yabbys)
        # dbsave.dbsave(fabrics_in_the_factory)

if __name__ == "__main__":
    main()
