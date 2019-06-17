import os

db_root = "/media/scott/cvmdata/Datasets/UCF-101"
num_of_folders = next(os.walk(db_root))
# print(num_of_folders[1])
# exit()


def read_img_names_from_dir(db_root=db_root):
    for root, dirs, files in os.walk(db_root):
        print(root)
        for name in files:
            print(root + "/" + name)


def read_img_names_from_txt(file):
    result = []
    with open(file, 'r') as f:
        for line in f:
            result.append(line)
    return result


def create_txt(arr, filename):
    if os.path.isfile(filename):
        open(filename, 'w').close()

    for rows in arr:
        with open(filename, "a+") as f:
            f.write(rows.replace("/media/6TB", "/media/scott/cvmdata/Datasets"))


# create_txt(read_img_names_from_txt("list/train.list"), "train.list")
create_txt(read_img_names_from_txt("list/test.list"), "test.list")

# x = nee.replace("/media/6TB", "/media/scott/cvmdata/Datasets")
