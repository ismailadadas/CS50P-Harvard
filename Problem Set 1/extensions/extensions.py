#file input
file = input("filename: ")
new_file = file.lower()
#if type pic print "image/type"
if '.gif' in new_file:
    print("image/gif")
elif '.png' in new_file:
    print("image/png")
elif '.jpg' in new_file:
    print("image/jpeg")
elif '.jpeg' in new_file:
    print("image/jpeg")
#if zip or pdf print "application/type"
elif '.pdf' in new_file:
    print("application/pdf")
elif '.zip' in new_file:
    print("application/zip")
#if txt print "text/plain"
elif '.txt' in new_file:
    print("text/plain")
#otherwise print "application/octet-stream"
else :
    print("application/octet-stream")
