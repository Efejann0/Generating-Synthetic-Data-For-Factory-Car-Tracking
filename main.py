import randomdatamatching as RandomDataMatching
import factorycircle as FactoryCircle
import databasesave as dbsave

count = 0

def main():
    global count
    fabrics_in_the_factory, yabbys = RandomDataMatching.t_zero_monent()
    dbsave.dbsave(fabrics_in_the_factory)
    while count <= 10000:
        fabrics_in_the_factory, yabbys = FactoryCircle.simulation_function(fabrics_in_the_factory, yabbys)
        dbsave.dbsave(fabrics_in_the_factory)
        count += 1

if __name__ == "__main__":
    main()
