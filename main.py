import shutil

file_path = 'sample.txt'

copy_light = """#       ::::::::::    :::     :::       ::::::::::       ::::::::       ::::::::      :::    :::           :::        :::::::::       ::::::::::
#      :+:           :+:     :+:       :+:             :+:    :+:     :+:    :+:     :+:    :+:         :+: :+:      :+:    :+:      :+:
#     +:+           +:+     +:+       +:+             +:+            +:+    +:+     +:+    +:+        +:+   +:+     +:+    +:+      +:+
#    +#++:++#      +#+     +:+       +#++:++#        +#++:++#++     +#+    +:+     +#+    +:+       +#++:++#++:    +#++:++#:       +#++:++#
#   +#+            +#+   +#+        +#+                    +#+     +#+    +#+     +#+    +#+       +#+     +#+    +#+    +#+      +#+
#  #+#             #+#+#+#         #+#             #+#    #+#     #+#    #+#     #+#    #+#       #+#     #+#    #+#    #+#      #+#
# ##########        ###           ##########       ########       ###########    ########        ###     ###    ###    ###      ##########
"""

# 元ファイルをバックアップして保存
back_name = file_path + '.bak'
shutil.copy(file_path, back_name)

# 元ファイルの情報を取得する
try:
    with open(file_path, encoding='utf-8') as f:
        source = f.read()

# 元ファイルを空にする

    with open(file_path, mode='w', encoding='utf-8') as f:
        f.write(copy_light)

# 元ファイルに文字列を書き込む

    with open(file_path, mode='a', encoding='utf-8') as f:
        f.write(source)
except:
    open_ex()


# except処理
def open_ex():
    print('ファイルをオープンできません')
    exit(1)
