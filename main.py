import os
import time

DAYS = 5
FOLDERS = [
    "/Users/Mariusmac/Desktop/Java"
]

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time()
ageTime = nowTime - 60 * 60 * 24 * DAYS


def delete_old_files(folder):
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILE += 1
                print("deleting file: " + str(fileName))
                os.remove(fileName)


def delete_emply_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            print("deleting empty dir: " + str(path))
            os.rmdir(path)


# =========================================


starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder)
    delete_emply_dir(folder)

finishtime = time.asctime()

print("=======================================================")

print("start: " + str(starttime))
print("total deleted size: " + str(TOTAL_DELETED_SIZE / 1024 / 1024) + "MB")
print("total deleted files: " + str(TOTAL_DELETED_FILE))
print("total deleted empty folders: " + str(TOTAL_DELETED_DIRS))
print("finish time :" + str(finishtime))

print("========================================================")
