import os
import yaml

# README.mdファイルを開き、マーカーまでの内容を読み込み
with open("README-ja.md", "r") as readme_file:
    readme_contents = ""
    for line in readme_file:
        readme_contents += line
        if line.strip() == "## List":
            break
    else:
        print("Marker not found in README-ja.md")
        exit(1)

# ファイルとディレクトリをスキャンし、新しいリンクを作成
categories = {}
for dirpath, dirnames, filenames in os.walk("./content/blog/"):
    if ".git" in dirpath or ".gitlab" in dirpath:
        continue  # Skip .git and .gitlab directories
    category = dirpath.lstrip("./content/blog/")
    for filename in filenames:
        if filename.endswith(".md") and filename != "README-ja.md":
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r") as file:
                content = file.read().split('---', 2)
                if len(content) < 3 or content[0].strip() != '':
                    continue  # Skip files without properly formatted front matter
                try:
                    til = yaml.safe_load(content[1])
                    if isinstance(til, dict):
                        title = til.get("title", "No title")
                        if category not in categories:
                            categories[category] = []
                        categories[category].append(f"- [{title}]({filepath})")
                except yaml.YAMLError:
                    print(f"Error reading file {filepath}")

# 更新した内容でREADME.mdファイルを再度書き込み
for category, links in categories.items():
    readme_contents += f"\n### {category}\n\n"
    readme_contents += '\n'.join(links)
    readme_contents += '\n'

with open("README-ja.md", "w") as readme_file:
    readme_file.write(readme_contents)
