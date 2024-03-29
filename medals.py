import json
import csv
import os

#CountryMedal object class with name, gold, silver, bronze and total attributes
class CountryMedals():
    def __init__(self, name, gold, silver, bronze):
        self.__name = str(name)
        self.__gold = int(gold)
        self.__silver = int(silver)
        self.__bronze = int(bronze)
        self.__total = self.__gold + self.__silver + self.__bronze
    # Function to output attributs to json format
    def to_json(self):
        json_dict = {"name": self.__name,"gold": self.__gold, "silver": self.__silver, "bronze": self.__bronze, "total": self.__total}
        return json.dumps(json_dict)
    
    #Setter and getter methods for all attributes
    def get_name(self):
        return self.__name
    
    def get_medals(self, medal_type):
        if medal_type.lower() == "gold":
            return self.__gold
        elif medal_type.lower() == "silver":
            return self.__silver
        elif medal_type.lower() == "bronze":
            return self.__bronze
        elif medal_type.lower() == "total":
            return self.__total
        else:
            print("Unknown medal type")
            return None
    #Function to output attributs to string format and print too console 
    def print_summary(self):
        summary_str = "{} received {} medals in total; {} gold, {} silver and {} bronze.".format(self.__name, 
                                                                                                 self.__total, 
                                                                                                 self.__gold, 
                                                                                                 self.__silver, 
                                                                                                 self.__bronze)
        print(summary_str)
    #Function to compare two CountryMedals objects and check the difference in medal types: gold, silver, bronze and total
    def compare(self, country_2):
        comparisons = []
        medal_comps = ["gold", "silver", "bronze", "total"]
        for medal in medal_comps:
            if medal == "total":
                if self.get_medals(medal) > country_2.get_medals(medal):
                    comparison = "Overall {} received {} medal(s), {} more than {}, which received {} medal(s).".format(self.__name, self.get_medals(medal),
                                                                                                                       (self.get_medals(medal) - country_2.get_medals(medal)), 
                                                                                                                       country_2.get_name(), country_2.get_medals(medal))
                    comparisons.append(comparison)
                elif self.get_medals(medal) < country_2.get_medals(medal):
                    comparison = "Overall {} received {} medal(s), {} less than {}, which received {} medal(s).".format(self.__name, self.get_medals(medal), 
                                                                                                                       (country_2.get_medals(medal)-self.get_medals(medal)), 
                                                                                                                       country_2.get_name(), country_2.get_medals(medal))
                    comparisons.append(comparison)
                else:
                    comparison = "Both {} and {} received {} medal(s).".format(self.__name, country_2.get_name(), self.get_medals(medal))
                    comparisons.append(comparison)
            else:
                if self.get_medals(medal) > country_2.get_medals(medal):
                    comparison = "{} received {} {} medal(s), {} more than {}, which received {}.".format(self.__name, self.get_medals(medal), medal,
                                                                                                         (self.get_medals(medal) - country_2.get_medals(medal)), 
                                                                                                         country_2.get_name(), country_2.get_medals(medal))
                    comparisons.append(comparison)
                elif self.get_medals(medal) < country_2.get_medals(medal):
                    comparison = "{} received {} {} medal(s), {} less than {}, which received {}.".format(self.__name, self.get_medals(medal), medal,
                                                                                                         (country_2.get_medals(medal)-self.get_medals(medal)), 
                                                                                                         country_2.get_name(), country_2.get_medals(medal))
                    comparisons.append(comparison)
                else:
                    comparison = "Both {} and {} received {} {} medal(s).".format(self.__name, country_2.get_name(), self.get_medals(medal), medal)
                    comparisons.append(comparison)
        print("\nCompare {} and {}.".format(self.__name, country_2.get_name()))
        print(*comparisons, sep='\n')

# Read a file medals.csv and create a dictionary 'countries' of CountryMedals objects
countries = {}
with open('medals.csv', 'r') as data:
    csv_data = csv.reader(data, delimiter=',')
    next(csv_data)
    for line in csv_data:
        country_medals = CountryMedals(line[1], line[2], line[3], line[4])
        countries[line[1]] = country_medals
#returnsl ist of countries sorted by their names
def get_sorted_list_of_country_names(countries):
    sorted_list = sorted(countries.keys())
    return sorted_list

#returns a list of countries sorted by a specific medal type in ascending order
def sort_countries_by_medal_type_ascending(countries, medal_type):
    sorted_list = sorted(countries.values(), key=lambda country: country.get_medals(medal_type))
    return sorted_list

#returns a list of countries sorted by a specific medal type in descending order
def sort_countries_by_medal_type_descending(countries, medal_type):
    sorted_list = sorted(countries.values(), key=lambda country: country.get_medals(medal_type), reverse=True)
    return sorted_list

#Helper function to input an integer value from the user and verify it is not empty and is a number
def read_positive_integer():
    try:
        int_input = int(input("Enter an integer greater than 0 (or enter 'q' to quit): "))
        if str(int_input).lower() == 'q' or str(int_input).lower() == 'quit':
            return str(int_input)
        else:
            if int_input < 0:
                print("Integer cannot be negative. Please try again.")
                return(read_positive_integer())
            return int_input
    except:
        print("Must be an integer value.")
        return(read_positive_integer())

#Helper Function to validate user input for a country name, validates that the country name is in the dictionary, is a string and is not empty
def read_country_name():
    input_country = input("Enter country name (or enter 'q' to quit): ")
    if input_country.lower() == 'q' or input_country.lower() == 'quit':
        return input_country
    else:
        try:
            if isinstance(float(input_country),float) == True:
                print("Must be a string value.")
                return(read_country_name())
        except:
            if input_country in countries.keys():
                if input_country == '':
                    print("Cannot be empty")
                    return(read_country_name())
                else: 
                    return input_country
            else:
                print("\nCountry not found (or input may have been in lower case), try again.")
                print("Here is a list of possible countries:")
                print(*get_sorted_list_of_country_names(countries), sep=', ')
                return(read_country_name())


#Helper function to enter medal type and validate it is a string and not empty, also validates it is a valid medal type
def read_medal_type():
    input_medal_type = input("Enter a medal type (choose between 'gold', 'silver', 'bronze' or 'total'): ")
    medal_types = ("gold", "silver", "bronze", "total")
    if input_medal_type.lower() == 'q' or input_medal_type.lower() == 'quit':
        return input_medal_type
    else:
        if input_medal_type in medal_types:
            if input_medal_type == '':
                print("Cannot be empty.")
                return(read_medal_type())
            try:
                if isinstance(float(input_medal_type),float) == True:
                    print("Must be a string value.")
                    return(read_medal_type())
            except:
                return input_medal_type
        else:
            print("Invalid medal type, please try again")
            return(read_medal_type())

#function to terrminat eexeecutioon loop, all helper functions output 'q' or 'quit' if user enters 'q' or 'quit' to send 
#the command to terminate the execution loop mid command
def terminate_loop():
    print("\nProgram Terminated. Goodbye!") 
    terminate = True
    return terminate

#Main function to run the program
def main():
    terminate = False
    while terminate == False:
        #Prompt user to enter a command
        user_input = input("\nEnter command (or enter 'H' for help): ")
        user_input = user_input.lower()
        #Validates if a command is entered to terminatee the loop
        if user_input == 'q' or user_input == 'quit':
            terminate = terminate_loop()
        #Priint list of countries and number of items in the dataset
        elif user_input == 'l' or user_input == 'list':
            print("The dataset contains {} countries: {}.".format(len(get_sorted_list_of_country_names(countries)), ", ".join(get_sorted_list_of_country_names(countries))))
        #Print a summary of a country's medals
        elif user_input == 's' or user_input == 'summary':
            country_name = read_country_name()
            if country_name.lower() == 'q' or country_name.lower() == 'quit':
                terminate = terminate_loop()
            else:
                selected_country = countries[country_name]
                selected_country.print_summary()
        #compare two countries ahd their medal counts
        elif user_input == 'c' or user_input == 'compare':
            country_name1 = read_country_name()
            if country_name1.lower() == 'q' or country_name1.lower() == 'quit':
                terminate = terminate_loop()
            else:
                country_name2 = read_country_name()
                if country_name2.lower() == 'q' or country_name2.lower() == 'quit':
                    terminate = terminate_loop()
                else:
                    selected_country1 = countries[country_name1]
                    selected_country2 = countries[country_name2]
                    selected_country1.compare(selected_country2)
        #Print a list of countries sorted by a specific medal type and more than a threshold in descending order
        elif user_input == 'm' or user_input == 'more':
            medal_type = read_medal_type()
            if medal_type.lower() == 'q' or medal_type.lower() == 'quit':
                terminate = terminate_loop()
            else:
                threshold = read_positive_integer()
                if str(threshold).lower() == 'q' or str(threshold).lower() == 'quit':
                    terminate = terminate_loop()
                else: 
                    country_medal_list = sort_countries_by_medal_type_descending(countries, medal_type)
                    print("Countries that received more than {} '{}' medal(s):".format(threshold, medal_type))
                    for country in country_medal_list:
                        if country.get_medals(medal_type) > threshold:
                            print("{} received {}".format(country.get_name(), country.get_medals(medal_type)))
        #Print a list of countries sorted by a specific medal type and less than a threshold in ascending order
        elif user_input == 'f' or user_input == 'fewer':
            medal_type = read_medal_type()
            if medal_type.lower() == 'q' or medal_type.lower() == 'quit':
                terminate = terminate_loop()
            else:
                threshold = read_positive_integer()
                if str(threshold).lower() == 'q' or str(threshold).lower() == 'quit':
                    terminate = terminate_loop()
                else: 
                    country_medal_list = sort_countries_by_medal_type_ascending(countries, medal_type)
                    print("Countries that received more than {} '{}' medal(s):".format(threshold, medal_type))
                    for country in country_medal_list:
                        if country.get_medals(medal_type) < threshold:
                            print("{} received {}".format(country.get_name(), country.get_medals(medal_type)))
        #export a summary of all countries to a file, filename is specified by the user and output to the samee directory as the program
        elif user_input == 'e' or user_input == 'export':
            file_name = input("Please enter a file name to export data as JSON: ")
            if file_name.lower() == "q" or file_name.lower() == "quit":
                terminate = terminate_loop()
            else:
                cwd = os.getcwd()
                with open("{}.json".format(file_name),"w") as f:
                    temp_dict = {}
                    for country in countries.keys():
                        country_json_dict = json.loads(countries[country].to_json())
                        temp_dict[country_json_dict["name"]] = {"gold" : country_json_dict["gold"], "silver" : country_json_dict["silver"] , 
                                                                "bronze" : country_json_dict["bronze"], "total" : country_json_dict["total"] }
                    json.dump(temp_dict, f, ensure_ascii=False, indent=4)
                    print("File successfully exported as '{}.json in the current directory: {}'".format(file_name, cwd))
        #list of availble commands
        elif user_input == 'h' or user_input == 'help':
            print("List of commands:")
            print("- (H)elp shows a list of available commands;")
            print("- (L)elp shows a list of countries in the dataset;")
            print("- (S)ummary shows a summary of medals won by a single country;")
            print("- (C)ompare allolws for a comparison of the medals woon by two countries;")
            print("- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;")
            print("- (F)ewer, given a medal type, lists all the countries that received fewer medals than a threshold;")
            print("- (E)xport, save the medalls dictionary as a '.json' file;")
            print("- (Q)uit.")
        else:
            print("Invalid Input, please try again or type 'H' to check for valid inputs")
            
if __name__ == "__main__":
    main()