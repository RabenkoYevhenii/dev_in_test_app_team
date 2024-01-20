import subprocess


def get_udid():
    cmd = ["adb", "devices"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.communicate()[0].decode("utf-8")

    devices = output.splitlines()[1:]
    if devices:
        udid = devices[0].split("\t")[0]
        return udid
    else:
        raise ValueError("No Android devices connected")
