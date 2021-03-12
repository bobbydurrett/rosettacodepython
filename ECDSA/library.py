import ecdsa

sk = ecdsa.SigningKey.generate() 

skstring = sk.to_string()

skint = int.from_bytes(skstring, "little")

print("\nSigning key = "+str(skint))

vk = sk.verifying_key

vkstring = vk.to_string()

vkint = int.from_bytes(vkstring, "little")

print("\nVerifying key = "+str(vkint))

msg ="Rosetta Code"
print("\nMessage: "+msg)

msgbytes = msg.encode("utf-8")

signature = sk.sign(msgbytes)

sigint = int.from_bytes(signature, "little")

print("\nSignature = "+str(sigint))




