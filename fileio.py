def fread(file_name):
    user_file=open('{}'.format(file_name),"rb")
    file_content=user_file.read()
    user_file.close()
    return file_content

def fwrite(file_name, towrite):
    user_file=open('{}'.format(file_name),"wb")
    user_file.write(towrite)
    user_file.close()
