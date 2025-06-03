import os
import shutil

def main():
    copy_static_files("static", "public")


def copy_static_files(source, target):
    if not os.path.exists(source):
        raise Exception("Invalid source path")

    if os.path.isfile(source):
        shutil.copy(source, target)
        return

    if os.path.exists(target):
        shutil.rmtree(target)

    os.mkdir(target)
    items = os.listdir(source)

    for item in items:
        if os.path.isfile(item):
            copy_static_files(os.path.join(source,item), target)
        else:
            copy_static_files(os.path.join(source, item),
                              os.path.join(target,item))


main()
