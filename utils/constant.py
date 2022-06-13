# 本文件是 CurseForgeModpackDownloader 的一部分。

# CurseForgeModpackDownloader 是自由软件：你可以再分发之和/或依照由自由软件基金会发布的 GNU 通用公共许可证修改之，无论是版本 3 许可证，还是（按你的决定）任何以后版都可以。

# 发布 CurseForgeModpackDownloader 是希望它能有用，但是并无保障；甚至连可销售和符合某个特定的目的都不保证。请参看 GNU 通用公共许可证，了解详情。

# 你应该随程序获得一份 GNU 通用公共许可证的复本。如果没有，请看 <https://www.gnu.org/licenses/>。
NAME = 'CurseForgeModpackDownloader'


class PATH:
    LOG_FILE_NAME = f'{NAME}.log'
    TEMP_DIR_PATH = f'.{NAME}'


class SEARCH:
    VERSIONS = ['', '1.10.2', '1.12.2', '1.16.5', '1.18.2']
    SORT = {
        'Name': 3,
        'Popularity': 1,
        'Total Downloads': 5
    }