import subprocess
import os



class crypto():
    def __init__(self, dirc, user):
        self.dir = dirc
        self.user = user

    def creatVolume(self):
        subprocess.call(["fallocate", "-l", "10M", "/home/" + self.user + '/' + self.user + "file"])
        subprocess.call(["cryptsetup", "-y", "luksFormat", "/home/" + self.user + '/' +self.user + "file"])
        subprocess.call(["sudo", "cryptsetup", "luksOpen", "/home/" + self.user + '/' + self.user + "file", self.user + "volume"])
        subprocess.call(["sudo", "mkfs.ext4", "/dev/mapper/" + self.user  + "volume"])


    def openVolume(self):
        subprocess.call(["sudo", "cryptsetup", "luksOpen", "/home/" + self.user + '/' + self.user + "file", self.user + "volume"])
        subprocess.call(["sudo", "mount", "/dev/mapper/" + self.user + "volume", "/home/" + self.user + "test" + self.user + "file"])

    def closeVolume(self):
        subprocess.call(["sudo", "umount", "/home/" + self.user + "test" + self.user + "file"])
        subprocess.call(["sudo", "cryptsetup", "luksOpen", self.user + "volume"])

if __name__ == "__main__":
    c = crypto("test", "guillaume")
    c.creatVolume()
