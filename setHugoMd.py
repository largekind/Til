import os
import datetime
import pathlib
import frontmatter

# './content/blog/'ディレクトリ以下のすべてのmarkdownファイルを取得
markdown_files = pathlib.Path('./content/blog').rglob('*.md')

for md_file in markdown_files:
    # ファイルを読み込む
    with open(md_file, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    # ファイルの作成時間を取得
    creation_time = datetime.datetime.fromtimestamp(md_file.stat().st_ctime)

    # カテゴリとタグの情報を取得
    relative_path = md_file.relative_to('./content/blog')
    categories = [relative_path.parts[0]]
    tags = [part for part in relative_path.parts[:-1]]  # タグの大文字小文字を維持

    # titleの情報を確認し、なければファイル名をタイトルとする
    if 'title' not in post.metadata or not post.metadata['title']:
        title = md_file.stem
        post.metadata['title'] = f'{title}'

    # dateの情報を確認し、なければ作成時間を追加
    if 'date' not in post.metadata or not post.metadata['date']:
        post.metadata['date'] = f'{creation_time}'

    # categoriesの情報を更新
    post.metadata['categories'] = f'["{categories[0]}"]'

    # tagsの情報を確認し、なければ追加
    if 'tags' in post.metadata:
        existing_tags = [tag.replace(' ', '') for tag in post.metadata['tags']]
        for tag in tags:
            if tag not in existing_tags:
                post.metadata['tags'].append(tag)
        post.metadata['tags'] = '[' + ', '.join(['"{}"'.format(tag) for tag in post.metadata['tags']]) + ']'
    else:
        post.metadata['tags'] = '[' + ', '.join(['"{}"'.format(tag) for tag in tags]) + ']'

    # ファイルに戻す
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        for key, value in post.metadata.items():
            if key == "title":
                f.write(f'{key}: "{value}"\n')  # タイトルは、ダブルクォーテーションで囲む
            elif isinstance(value, datetime.datetime):
                value = value.isoformat(timespec='seconds') #時刻情報はHugoの形式(ISO8601)にする
                f.write(f'{key}: {value}\n')
            else:
                f.write(f'{key}: {value}\n')
        f.write('---\n')
        f.write(post.content)
