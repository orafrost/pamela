from subprocess import Popen, PIPE, STDOUT
import os



class crypto():
    def __init__(self, dirc, user):
        self.dir = dirc
        self.user = user

    def creatVolume(self):
        p  = Popen(["fallocate", "-l", "10M", "/home/" + self.user + '/' + self.user + "file"], stdin=PIPE, stderr=STDOUT)
        p = Popen(["cryptsetup", "-y", "luksFormat", "/home/" + self.user + '/' +self.user + "file"], stdin=PIPE, stderr=STDOUT)
        p.communicate(input=b'YES\n')
        p = Popen(["sudo", "cryptsetup", "luksOpen", "/home/" + self.user + '/' + self.user + "file", self.user + "volume"], stdin=PIPE, stderr=STDOUT)
        p = Popen(["sudo", "mkfs.ext4", "/dev/mapper/" + self.user  + "volume"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)


    def openVolume(self):
        p = Popen(["sudo", "cryptsetup", "luksOpen", "/home/" + self.user + '/' + self.user + "file", self.user + "volume"], stdin=PIPE, stderr=STDOUT)
        p = Popen(["sudo", "mount", "/dev/mapper/" + self.user + "volume", "/home/" + self.user + "test" + self.user + "file"], stdin=PIPE, stderr=STDOUT)

    def closeVolume(self):
        p = Popen(["sudo", "umount", "/home/" + self.user + "test" + self.user + "file"], stdin=PIPE, stderr=STDOUT)
        p = Popen(["sudo", "cryptsetup", "luksOpen", self.user + "volume"], stdin=PIPE, stderr=STDOUT)

if __name__ == "__main__":
    c = crypto("test", "guillaume")
    c.closeVolume()
