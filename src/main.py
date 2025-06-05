import os
from os.path import isfile
import shutil
from pathlib import Path
from html_conversion import extract_title, markdown_to_html_node

def main():
    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")


def copy_static_files(source, target):
    if not os.path.exists(source):
        raise Exception("Invalid source path")

    if os.path.isfile(source):
        shutil.copy(source, target)
        return

    if os.path.exists(target):
        shutil.rmtree(target)

    os.mkdir(target)
    items = os.listdir(source)

    for item in items:
        if os.path.isfile(item):
            copy_static_files(os.path.join(source,item), target)
        else:
            copy_static_files(os.path.join(source, item),
                              os.path.join(target,item))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    result = ""
    with open(from_path) as from_file, open(template_path) as template_file:
        template = template_file.read()
        content = from_file.read()
        content_html = markdown_to_html_node(content).to_html()
        title = extract_title(content)
        result = template.replace("{{ Title }}", title)
        result = result.replace("{{ Content }}", content_html)

    target = Path(dest_path)
    target.parent.mkdir(exist_ok=True, parents=True)

    with target.open("w") as target_file:
        target_file.write(result)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        relative_path = os.path.join(dir_path_content, item)
        relative_dest = os.path.join(dest_dir_path, item).replace(".md",
                                                                  ".html")

        if os.path.isfile(relative_path) and item.endswith(".md"):
            generate_page(relative_path, template_path, relative_dest)
        elif not os.path.isfile(relative_path):
            generate_pages_recursive(relative_path,template_path, relative_dest)


main()
