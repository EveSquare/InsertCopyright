import shutil

# file_path = 'sample.txt'


def write_file(path):

    copy_light = """#       ::::::::::    :::     :::       ::::::::::       ::::::::       ::::::::      :::    :::           :::        :::::::::       ::::::::::
#      :+:           :+:     :+:       :+:             :+:    :+:     :+:    :+:     :+:    :+:         :+: :+:      :+:    :+:      :+:
#     +:+           +:+     +:+       +:+             +:+            +:+    +:+     +:+    +:+        +:+   +:+     +:+    +:+      +:+
#    +#++:++#      +#+     +:+       +#++:++#        +#++:++#++     +#+    +:+     +#+    +:+       +#++:++#++:    +#++:++#:       +#++:++#
#   +#+            +#+   +#+        +#+                    +#+     +#+    +#+     +#+    +#+       +#+     +#+    +#+    +#+      +#+
#  #+#             #+#+#+#         #+#             #+#    #+#     #+#    #+#     #+#    #+#       #+#     #+#    #+#    #+#      #+#
# ##########        ###           ##########       ########       ###########    ########        ###     ###    ###    ###      ##########
"""    

    # 元ファイルをバックアップして保存
    back_name = path + '.bak'
    shutil.copy(path, back_name)

    # 元ファイルの情報を取得する
    try:
        with open(path, encoding='utf-8') as f:
            source = f.read()

    # 元ファイルを空にする

        with open(path, mode='w', encoding='utf-8') as f:
            f.write(copy_light)

    # 元ファイルに文字列を書き込む

        with open(path, mode='a', encoding='utf-8') as f:
            f.write(source)
    except:
        open_ex()


# except処理
def open_ex():
    print('ファイルをオープンできません')
    exit(1)
