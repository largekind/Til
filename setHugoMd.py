# content/blog内にあるmarkdownに対して、日付とtitleを自動追加する

import glob
import re
import os
import datetime

filelist = glob.glob('./content/**/*.md',recursive=True)
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
    if not lines[0] == '---':
      Buf.append('---\n')
      UseHugoFirst = True
    # ファイルにHugoで必要なTitleが無いなら追記
    if not "title:" in lines:
      # markdownのtitle行を取得する
      l_re_match = [s for s in lines if re.match('^# .*$', s)]
      Buf.append('title: '+'\"'+l_re_match[0].replace("# ","").replace("\n","") +'\"\n')

    # ファイルにHugoで必要なDateが無いなら追記 自動的に後からgitでコミットした更新日が入るので、ここでは適当
    if not "date:" in lines:
      now = datetime.datetime.today().strftime("%Y-%m-%d")
      Buf.append('date: '+now+'T00:00:00+09:00'+'\n')
      Buf.append('lastmod: ''\"'+now+'\"'+'\n')

    # Hugo未使用だった場合は最後の---を追記
    if UseHugoFirst == True:
      Buf.append('---\n')
    print(Buf)

    # ファイルの先頭に行追加
    with open(path,'w') as f:
      f.writelines(Buf)
      f.writelines(lines)
