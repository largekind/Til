import os
import yaml

# README.mdファイルを開き、マーカーまでの内容を読み込みます
with open("README.md", "r") as readme_file:
    readme_contents = ""
    for line in readme_file:
        readme_contents += line
        if line.strip() == "##List ":
            break
    else:
        print("Marker not found in README.md")
        exit(1)

# ファイルとディレクトリをスキャンし、新しいリンクを作成します
for dirpath, dirnames, filenames in os.walk("."):
    if ".git" in dirpath or ".gitlab" in dirpath:
        continue  # Skip .git and .gitlab directories
    for filename in filenames:
        if filename.endswith(".md") and filename != "README.md":
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r") as file:
                try:
                    til = yaml.safe_load(file)
                    category = dirpath.lstrip("./")
                    title = til.get("title", "No title")
                    readme_contents += f"- [{category}: {title}]({filepath})\n"
                except yaml.YAMLError:
                    print(f"Error reading file {filepath}")

# 更新した内容でREADME.mdファイルを再度書き込みます
with open("README.md", "w") as readme_file:
    readme_file.write(readme_contents)
