#!/usr/bin/python3
import os
import yaml  # external libary


def fstab(val="fstab.yaml"):

    with open(val, "r") as yamlfile:                                        #read yaml file
        data = yaml.safe_load(yamlfile)



    output: str=""
 #   try:
    for sub in data['fstab']:

        if (data['fstab'][sub]["type"]) == "nfs":
            output += (str(sub)+":" +data['fstab'][sub]["export"]  + " ")  # add fstab colums to string
            output += ((data['fstab'][sub]["mount"]) + " ")
            output += (data['fstab'][sub]["type"] + " ")
        else:
            output+=(str(sub) +" ")                          #add fstab sections to string
            output+=((data['fstab'][sub]["mount"])+" ")
            output+=(data['fstab'][sub]["type"]+" ")

        try:                                             #add optional values to string

            for opt in data['fstab'][sub]["options"]:
                output+=(opt+  ",")
        except:pass

        output+=("\n")                                  #add new line to string








    return output










if __name__ == '__main__':
        yamls = input("Enter path to yaml file: ")                                          # get path to yaml file
        if yamls == '': yamls ="fstab.yaml"                                                 # assume filename when input is ommited


        out = fstab(yamls)
        with open("fstab", "a") as text_file:                                               # write fstab to file
            text_file.write(out)

        print("Checking fstab...")
        try:
            os.system("findmnt --verify --verbose ./fstab")                                 # only works on unix

        except:print("Can not check fstab, please run \"findmnt --verify --verbose ./fstab\" on unix.")