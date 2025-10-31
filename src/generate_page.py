from markdown_to_html import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    dest_path = f"{dest_path[0:-2]}html"
    
    print(f"""Generating page from --{from_path}-- 
          to --{dest_path}-- 
          using --{template_path}--""")
    print()

    md_file = open(from_path)
    template_file = open(template_path)

    md_content = md_file.read()
    template_content = template_file.read()
    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)
    html_string_full = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    html_string_full = html_string_full.replace("href=/", f"href={basepath}").replace("src=/", f"src={basepath}")

    # if os.path.isfile(dest_path):
    with open(dest_path, "w") as file:
        file.write(html_string_full)

    md_file.close()
    template_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.exists(dir_path_content):
        content_list = os.listdir(dir_path_content)
        for content in content_list:
            content_path = os.path.join(dir_path_content, content)
            if os.path.isfile(content_path):
                dest_file_path = os.path.join(dest_dir_path, content)
                generate_page(content_path, template_path, dest_file_path, basepath)
            elif os.path.isdir(content_path):
                new_dir_path = os.path.join(dest_dir_path, content)
                os.mkdir(new_dir_path)
                generate_pages_recursive(content_path, template_path, new_dir_path, basepath)