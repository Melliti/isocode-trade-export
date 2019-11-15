import sys

class dataManager:
    # If users do not add special parameter to the program
    # results are displayed
    def printValues(self, countries):
        for country in countries:
            print(country)

    # Put results in a CSV. Name can be passed as third parameter
    def csvValues(self, countries):
        try:
            f = open(sys.argv[3],"w")
        except:
            f = open("save.csv","w")
            pass
        f.write("ISO,VALUE\n")
        for country in countries:
            datas = country.split(" ")
            f.write(datas[1] + "," + datas[2] + "\n")
        f.close
            

            