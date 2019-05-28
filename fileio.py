def fread(file_name):
    user_file=open(file_name,"r")
    file_content=user_file.read()
    user_file.close()
    return str(file_content)

def fwrite(file_name, towrite):
    user_file=open(file_name,"w")
    user_file.write(towrite)
    user_file.close()

def read_dict_from_file(f_name):
    with open('{}'.format(f_name)) as f:
        d = dict(x.rstrip().split(None, 1) for x in f)
        return d
