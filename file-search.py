import pathlib


# list to store all images name
image_list = []
# file format you want to be searched
file_type = ".png"

######  STARITING POINT ##########
# declare the starting point
start_point_path = "G:\FORMODE\ARCHIVED PROJECTS"

# create an object of the starting point
start_point_path_obj = pathlib.Path(start_point_path)

#########  lEVEL 1 ##########

for level_1 in start_point_path_obj.iterdir():
    # check if it's a file
    if level_1.is_file():
        # check for images
        if level_1.suffix ==f"{file_type}":
            level_1_name = level_1.name
            image_list.append(start_point_path + '\\' + level_1_name)

    
    #if it's not a file then it is a directory
    else:
        # generate path object for level 2

        # name of level 1 folders
        level_1_name = level_1.name
    
        # path of level 1 folders
        level_1_path = start_point_path + '\\' + level_1_name
    
        # create an object of pathlib.path project_path
        level_1_path_obj = pathlib.Path(level_1_path)

        #########  lEVEL 2 ##########

        for level_2 in level_1_path_obj.iterdir():
            if level_2.is_file():
                # check for images
                if level_2.suffix ==f"{file_type}":
                    level_2_name = level_2.name
                    image_list.append(level_1_path + '\\' + level_2_name)  

            else:
                # name of level 2 folders
                level_2_name = level_2.name
        
                # path of level 2 folders
                level_2_path = level_1_path + '\\' + level_2_name
        
                # create an object of pathlib.path project_path
                level_2_path_obj = pathlib.Path(level_2_path)

                #########  lEVEL 3 ##########

                for level_3 in level_2_path_obj.iterdir():

                    if level_3.is_file():
                        # check for images
                        if level_3.suffix == f"{file_type}":
                            level_3_name = level_3.name
                            image_list.append(level_2_path + '\\' + level_3_name)  

# print all images gathered
for files in image_list:
    print(files)   