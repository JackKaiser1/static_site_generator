from markdown_to_html import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file = open(from_path)
    md_content = md_file.read()

    template_file = open(template_path)
    template_content = template_file.read()

    html_content = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)

    html_string_full = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    with open(dest_path, "w") as file:
        file.write(html_string_full)

    md_file.close()
    template_file.close()