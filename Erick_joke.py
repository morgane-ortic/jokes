import subprocess

msg1 = " Did you hear about the first restaurant to open on the moon?"
msg2 = "It had great food, but no atmosphere."

msg = msg1 + msg2
subprocess.call(["cowsay", msg])

