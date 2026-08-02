import qrcode
print("=====QR Code Generator=====")
data=input("enter text or url:")
img=qrcode.make(data)
file_name=input("enter file name(without .png):")
img.save(file_name+".png")
print(f"\n QR code Generated successfully!")
print(f"saved as:{file_name}.png")