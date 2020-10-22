
import os


def main():
    os.chdir("FilesToSort")
    # I didnt have this ^^ at first and was having loads of trouble. So looked at the answers. Seems obvious now. But i couldent figure it out for some reason
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        os.rename(filename, "{}/{}".format(extension, filename))

main()
