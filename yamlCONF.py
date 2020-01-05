import yaml, glob, argparse
from argparse import RawTextHelpFormatter


# Location where your YAML rules are defined
rule_repo = glob.glob('C:\\Users\\Phil\\Desktop\\Code\\YAMLconf\Rules\\*.yaml')

# Where you want your savedsearches.conf to go
output_file = open('C:\\Users\\Phil\\Desktop\\Code\\YAMLconf\\savedsearches.conf', 'w')

def yaml_in_conf_out(filename):
    with open(filename, 'r') as stream:
        try:
            rule_list = yaml.safe_load(stream)
            title = rule_list['title']
            search = rule_list['configuration']['search'][0]

            # Output required fields to created savedsearches.conf
            output_file.write("\n" + "["+ title + "]" + "\n")
            output_file.write('search = ' + str(search) + "\n")

        except yaml.YAMLError as exc:
            print(exc)




def main():

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)#(description='Process some stuff.')
    parser.add_argument('-a', dest='action', type=str, default="", help='action to execute. Two supported\n\'import\' will convert a savedsearches.conf to individual YAML files. \n\'export\' will convert individual YAML files to a savedsearches.conf.')
    results = parser.parse_args()

    action = results.action

    if (action):
        if (action == "export"):
            print("exported")
            for file in rule_repo:
                yaml_in_conf_out(file)
        
        if (action == "import"):
            print("imported")
        


    else:
        parser.print_help()

if __name__ == '__main__':

    try:
       main()

    except KeyboardInterrupt:
        print("\n")
        print ("[!] Exiting")
        sys.exit()