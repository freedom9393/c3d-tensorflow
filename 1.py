import os
import subprocess
import csv

os.chdir("/media/scott/cvmdata/Datasets/GRRC/Dataset")
save_dir = "/media/scott/cvmdata/Datasets/GRRC/Sabr/"
actions = ["walk", "go_out", "empty_room", "go_in", "walk", "sit", "walk", "falling"]
with open('dataset.csv', 'r') as f:
    file_num = 3
    zet = 1000
    reader = csv.reader(f)
    your_list = list(reader)
    bitch = []
    for i in range(len(your_list)):
        nums = your_list[i]
        for j in range(len(nums)-1):
            if float(nums[j]) >= 60.0:
                start = "00:01:" + "00" if float(nums[j]) - 60.0 == 0 else str(float(nums[j]) - 60.0) if float(nums[j]) >= 60.0 else str(0) + str(float(nums[j]) - 60.0)
                finish = "00:00:0" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3)) if abs(
                        float(nums[j]) - float(nums[j + 1])) < 10.0 else "00:00:" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3))
                # print(file_num, start, stop, "katta")
                subprocess.run(["ffmpeg", "-i", str(file_num) + ".avi", "-ss", start,
                                "-t", finish, "-vcodec", "rawvideo",
                                save_dir + actions[j] + "/" + str(file_num) + "_" + str(zet) + ".avi"])
            else:
                # print(file_num, "00:00:" + nums[j] if float(nums[j]) >= 10.0 else "00:00:0" + nums[j], "00:00:0" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3)) if abs(
                #         float(nums[j]) - float(nums[j + 1])) < 10.0 else "00:00:" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3)))
                start = "00:00:" + nums[j] if float(nums[j]) >= 10.0 else "00:00:0" + nums[j]
                stop = "00:00:0" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3)) if \
                    round(abs(float(nums[j]) - float(nums[j + 1])), 3) < 10.0 else "00:00:" + str(round(abs(float(nums[j]) - float(nums[j + 1])), 3))
                # print(file_num, start, stop, "kichik", round(abs(float(nums[j]) - float(nums[j + 1])), 3))
                subprocess.run(["ffmpeg", "-i", str(file_num) + ".avi", "-ss", start,
                                "-t", stop, "-vcodec", "rawvideo",
                                save_dir + actions[j] + "/" + str(file_num) + "_" + str(zet) + ".avi"])
            zet += 1
        file_num += 1

# for folders in os.listdir(save_dir):
#     num = 1
#     for video in os.listdir(save_dir+folders):
#         print(folders, video)
#         os.rename(save_dir+folders+"/"+video, save_dir+folders+"/"+folders+str(num)+".avi")
#         num += 1
