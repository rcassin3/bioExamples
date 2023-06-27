import os

#
# Global variable containing all the keys
#
keys = ["SNP", "Clinical_Relevance", "Gene", "Type", "Chromosome", "Position", "Region"]

# =========================
# Define GeneRegistry class
# =========================
class GeneRegistry:
    def __init__(self):
        self.registry_name = ""
        self.SNPs = []
        self.changed = False
        self.regFile = ""
        self.filename = ""
        self.registry_opened = False

    def __str__(self):
        fileobject = open(self.regFile, 'r')
        return fileobject.read()
        fileobject.close()
        registry.changed = False

    def load_from_file(self, filename):
        # 1. Check if the file exists
        if os.path.exists(filename):
            self.regFile = filename
            readFile = open(filename, 'r')
            self.registry_name = readFile.readline()
            i = int(readFile.readline())
            while i > 0:
                self.SNPs.append(readFile.readline(10))
                readFile.readline()
                i -= 1
            readFile.close()
            #
            # If a file exists, load the data from the file
            # Replace the placeholder pass
            #pass
        else:
            c = input(
                filename
                + " doesn't exist. Do you want to create a new registry? (y/n)\n"
            )
            if c == "y":
                e = input(
                    "Input desired registry name:\n"
                )
                self.registry_name = "{}" + e + "() registry"
                self.regFile = filename
                self.SNPs = []
                fileobject = open(filename, 'w')
                fileobject.write(self.registry_name + "\n0\n")
                fileobject.close()
                # Create an empty registry
                # Replace the placeholder pass
                #pass
            else:
                return
        self.registry_opened = True

    def add_snp_from_file(self, filename):
        # 1. Check if the file exists
        if os.path.exists(filename):
            snpFile = open(filename, 'r')
            regFile = open(self.regFile, 'a')
            snpFormat = snpFile.readlines()
            snpFile.seek(0, 0)
            i = 0
            while i < 7:
                if "\n" in snpFormat[6]:
                    if i < 6:
                        regFile.write(snpFile.readline().replace("\n", "\t"))
                    else:
                        regFile.write(snpFile.readline())
                else:
                    if i < 6:
                        regFile.write(snpFile.readline().replace("\n", "\t"))
                    else:
                        regFile.write(snpFile.readline() + "\n")
                i += 1
            snpFile.close()
            regFile.close()
            regFile = open(self.regFile, 'r')
            lines = regFile.readlines()
            regFile.close()
            n = len(lines)
            tempFile = open(self.regFile, 'w+')
            counter = 0
            while counter < n:
                if counter == 1:
                    snpFile = open(filename, 'r')
                    self.SNPs.append(snpFile.readline(10))
                    snpFile.close()
                    tempFile.write(str(len(self.SNPs)) + "\n")
                else:
                    tempFile.write(lines[counter])
                counter += 1
            tempFile.close()
            self.changed = True
            



            # If a file exists, add the data from the file
            # Replace the placeholder pass
            #pass
        else:
            input(filename + " doesn't exist. Press any key to continue...\n")

    def save_to_file(self):
        fileobject = open(self.regFile, 'r')
        if os.path.exists(self.filename):
            newFile = open(self.filename, 'w')
            newFile.write(fileobject.read())
            fileobject.close() 
            newFile.close()
        else:
            fileobject.close()  
        #
        # Write the registry to a file in the same format as my_reg.data
        # Replace the placeholder pass
        # pass

    def delete_snp(self, idx):
        regFile = open(self.regFile, 'r')
        snpLines = regFile.readlines()
        removedSNP = snpLines[idx + 2][:10]
        del snpLines[idx + 2]
        n = len(snpLines)
        regFile.close()
        tempFile = open(self.regFile, 'w+')
        counter = 0
        while counter < n:
            if counter == 1:
                self.SNPs.remove(removedSNP)
                tempFile.write(str(len(self.SNPs)) + "\n")
            else:
                tempFile.write(snpLines[counter])
            counter += 1
        tempFile.close()
        self.changed = True


        # Delete the SNP as the given idx position
        #
        # Replace the placeholder pass
        # pass

    def search_registry(self, query_key, query_value):
        count = 0

        regFile = open(self.regFile, 'r')
        snpLines = regFile.readlines()
        regFile.close()
        del snpLines[:2]
        for element in snpLines:
            SNP, Clinical_Relevance, Gene, Ttype, Chromosome, Position, Region = element.split("\t")
            if query_key == "SNP":
                if query_value in SNP:
                    count += 1
            if query_key == "Clinical_Relevance":
                if query_value in Clinical_Relevance:
                    count += 1
            if query_key == "Gene":
                if query_value in Gene:
                    count += 1
            if query_key == "Type":
                if query_value in Ttype:
                    count += 1
            if query_key == "Chromosome":
                if query_value in Chromosome:
                    count += 1
            if query_key == "Position":
                if query_value in Position:
                    count += 1
            if query_key == "Region":
                if query_value in Region:
                    count += 1
        
        

        if count > 0:
            input(
                "Found " + str(count) + " SNP(s)! " + "Press any key to continue...\n"
            )
        else:
            input("No SNP found! " + "Press any key to continue...\n")




# function to print the main menu of the registry program
def print_main_menu():
    selection = 0
    os.system("cls" if os.name == "nt" else "clear")
    print("*************************************")
    print("***       Registry main menu      ***")
    print("*************************************")
    print("***                               ***")
    print("*** 1 -> Create or Load registry  ***")
    print("*** 2 -> Show registry content    ***")
    print("*** 3 -> Add entry to registry    ***")
    print("*** 4 -> Search registry          ***")
    print("*** 5 -> Delete registry entry    ***")
    print("*** 6 -> Quit the program         ***")
    print("***                               ***")
    print("*************************************")

    i = input("---> Select option : ")
    try:
        selection = int(i)
    except ValueError:
        print("\nInvalid integer input")
        selection = -1

    return selection


# This is the "main" function
if __name__ == "__main__":

    # Create an object of the GeneRegistry
    registry = GeneRegistry()

    selection = 0
    while selection != 6:
        # print the main menu of the program
        selection = print_main_menu()
        if selection == 1:
            fn = input("\nPlease enter registry file name: ")
            registry.load_from_file(fn)
        elif selection > 1 and selection < 6:
            if registry.registry_opened:
                if selection == 2:
                    print(registry)
                    input("Press enter to continue ...\n")
                elif selection == 3:
                    fn = input("\nPlease enter snp file name: ")
                    registry.add_snp_from_file(fn.strip())
                elif selection == 4:
                    query_key = input("\nPlease enter query key: ")
                    query_value = input("Please enter query value: ")
                    registry.search_registry(query_key, query_value)
                elif selection == 5:
                    ss = input("\nPlease enter snp index to delete: ")
                    idx = int(ss)
                    registry.delete_snp(idx)
            else:
                input("No registry opened! Press enter to continue...\n")

        if registry.changed:
            c = input("\nSave the registry? (y/n)")
            if c == "y":
                registry.save_to_file()

