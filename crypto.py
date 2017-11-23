from subprocess import call
import os



class crypto():
    def __init__(self, dirc, user, passwd):
        self.dir = dirc
        self.user = user
        self.passwd = passwd

    def creatVolume(self):
        call("fallocate -l 10M /home/" + self.user + '/' + self.user + "file", shell=True)
        call("echo " + self.passwd + " | cryptsetup -q luksFormat /home/" + self.user + '/' +self.user + "file", shell=True)
        call("echo " + self.passwd + " | sudo cryptsetup luksOpen /home/" + self.user + '/' + self.user + "file" + " " + self.user + "volume", shell=True)
        call("sudo mkfs.ext4 /dev/mapper/" + self.user  + "volume", shell=True)


    def openVolume(self):
        call("sudo cryptsetup luksOpen /home/" + self.user + '/' + self.user + "file" + " " + self.user + "volume", shell=True)
        call("sudo mount /dev/mapper/" + self.user + "volume" + " " + "/home/" + self.user + "test" + self.user + "file", shell=True)

    def closeVolume(self):
        call("sudo umount /home/" + self.user + "test" + self.user + "file"], shell=True)
        call("sudo cryptsetup luksOpen" + " " + self.user + "volume", shell=True)

if __name__ == "__main__":
    c = crypto("test", "guillaume", "test")
    c.creatVolume()
