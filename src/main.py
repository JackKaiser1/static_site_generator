from textnode import TextNode
from type_enums import TextType
import os
import shutil

def main():
    dst_dir = "public"
    src_dir = "static"
    working_dir = "/home/jackk/dev/github.com/jackkaiser1/static_site_generator/"
    del_and_copy(working_dir, dst_dir, src_dir)

def del_and_copy(working_dir, dst_dir, src_dir):
    source_path = os.path.join(working_dir, src_dir)
    destination_path = os.path.join(working_dir, dst_dir)
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
        os.mkdir(destination_path)
        copy_dir(source_path, destination_path)
    else:
        raise Exception("The provided directory does not exist")
    
    
def copy_dir(source_path, destination_path):
    if os.path.exists(source_path):
        dir_content = os.listdir(source_path)
        for content in dir_content:
            content_path = os.path.join(source_path, content)
            if os.path.isfile(content_path):
                shutil.copy(content_path, destination_path)
            elif os.path.isdir(content_path):
                dir_path = os.path.join(destination_path, content)
                os.mkdir(dir_path)
                copy_dir(content_path, dir_path)
    print(os.listdir(destination_path))


    



main()
