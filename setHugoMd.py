import os
import datetime
import pathlib
import frontmatter

# './content/blog/'ディレクトリ以下のすべてのmarkdownファイルを取得
markdown_files = pathlib.Path('./content/blog').rglob('*.md')

for md_file in markdown_files:
    # ファイルを読み込む
    with open(md_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
        post = frontmatter.loads(original_content)

    # ファイルの作成時間を取得
    creation_time = datetime.datetime.fromtimestamp(md_file.stat().st_ctime)

    # カテゴリとタグの情報を取得
    relative_path = md_file.relative_to('./content/blog')
    new_category = relative_path.parts[0]
    tags = [part for part in relative_path.parts[:-1]]

    # titleの情報を確認し、なければファイル名をタイトルとする
    if 'title' not in post.metadata or not post.metadata['title']:
        title = md_file.stem
        post.metadata['title'] = title

    # dateの情報を確認し、なければ作成時間を追加
    if 'date' not in post.metadata or not post.metadata['date']:
        post.metadata['date'] = creation_time.isoformat(timespec='seconds')

    # categoriesの情報を確認し、なければ追加
    if 'categories' not in post.metadata:
        post.metadata['categories'] = [new_category]
    else:
        existing_categories = post.metadata['categories']
        if not any(new_category.lower() == cat.lower() for cat in existing_categories):
            post.metadata['categories'].append(new_category)

    # tagsの情報を確認し、なければ追加
    if 'tags' in post.metadata:
        existing_tags = post.metadata['tags']
        for tag in tags:
            if not any(tag.lower() == t.lower() for t in existing_tags):
                post.metadata['tags'].append(tag)
    else:
        post.metadata['tags'] = tags

    # 更新された内容を構築
    updated_content = '---\n'
    for key, value in post.metadata.items():
        if key == "title":
            updated_content += f'{key}: "{value}"\n'
        elif isinstance(value, datetime.datetime):
            updated_content += f'{key}: {value.isoformat(timespec="seconds")}\n'
        elif isinstance(value, list):
            formatted_list = '[' + ', '.join([f'"{item}"' for item in value]) + ']'
            updated_content += f'{key}: {formatted_list}\n'
        else:
            updated_content += f'{key}: {value}\n'
    updated_content += '---\n'
    updated_content += post.content

    # 元のファイルの末尾が改行で終わっていれば、改行を追加
    if original_content.endswith('\n'):
        updated_content += '\n'

    # 変更がない場合はファイルを書き戻さない
    if original_content != updated_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
