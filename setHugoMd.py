# content/blog内にあるmarkdownに対して、日付とtitleを自動追加する

import glob
import re
import os
import datetime
import itertools

filelist = glob.glob('./content/blog/**/*.md',recursive=True)
#print(l)

# 各ファイルごとに処理
for path in filelist:
    # ファイル読み込み
    print("filepath : ",path)
    with open(path) as f:
      lines = f.readlines()
    # 追加する用のバッファ定義
    Buf = []
    UseHugoFirst = False #Hugoが一切使用されてないかチェック用フラグ
    # 先頭行に"---"が無いなら追記 Hugoが一切使われてない事がわかるのでフラグを立てる
    if not lines[0] == '---\n':
      Buf.append('---\n')
      UseHugoFirst = True

    # ファイルにHugoで必要なTitleが無いなら追記
    if not any("title: " in word for word in lines):
      # markdownのtitle行を取得する
      l_re_match = [s for s in lines if re.match('^# .*$', s)]
      Buf.append('title: '+'\"'+l_re_match[0].replace("# ","").replace("\n","") +'\"\n')

    # ファイルにHugoで必要なDateが無いなら追記 自動的に後からgitでコミットした更新日が入るので、ここでは適当
    if not any("date: " in word for word in lines):
      now = datetime.datetime.today().strftime("%Y-%m-%d")
      Buf.append('date: '+now+'T00:00:00+09:00'+'\n')

    # 自分がいる場所のTagがない場合は付与
    if not any("tags: " in word for word in lines):
      #blog/以降のディレクトリパスを取得し、必要部分だけ抜粋
      dirtags = os.path.dirname(path).replace("./content/blog/","").split("/")
      Buf.append('tags: ['+ ','.join(str(tag) for tag in dirtags) +']\n')
      print("DirTag:",dirtags)

    # 自分がいる場所のcategoriesがない場合は付与
    if not any("categories: " in word for word in lines):
      #blog/以降のディレクトリパスを取得し、必要部分だけ抜粋
      categories = os.path.dirname(path).replace("./content/blog/","").split("/")[0]
      Buf.append('categories: ['+ categories +']\n')
      print("categories:",categories)

    # Hugo未使用だった場合は最後の---を追記
    if UseHugoFirst == True:
      Buf.append('---\n')
    print(Buf)

    # ファイルの先頭に行追加
    with open(path,'w') as f:
      #何かしらBufがあるならHead formatterの最後に追記
      if len(Buf) != 0:
        if UseHugoFirst == True:
          #Hugo初回ならそのままBufを先頭に書き込む
          f.writelines(Buf)
        else:
          #HugoのHeader最後に追記
          index = [i for i, x in enumerate(lines) if x == '---\n'][1]
          print("last format index:"+str(index))
          for buf in Buf: lines.insert(index, buf)
      f.writelines(lines)
