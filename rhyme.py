from pypinyin import pinyin
from pypinyin.constants import TONE3


def handle(c):
    s = pinyin(c, heteronym=True, style=TONE3, strict=False)
    return s[0]


def cut(s):
    if len(s) >= 2:
        if s[0:2] in ['zh', 'ch', 'sh']:
            return s[0:2], s[2:]
        elif s[0] in ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'z', 'c', 's', 'r', 'y',
                      'w']:
            return s[0], s[1:]
    return '', s


# yunmu -> char
results = {}

if __name__ == '__main__':
    with open('chars', encoding='utf-8') as f:
        ss = f.read()
        for s in ss[0:4000]:
            c = handle(s)

            for cc in c[0:1]:
                sy = cut(cc)
                key = sy[1]
                if sy[1] in ['i', 'i1', 'i2', 'i3', 'i4']:
                    # additional categorize by shengmu
                    if sy[0] in ['zh', 'ch', 'sh', 'r']:
                        key = 'r' + sy[1]
                    elif sy[0] in ['z', 'c', 's']:
                        key = 'z' + sy[1]
                if sy[1] in ['e', 'e1', 'e2', 'e3', 'e4']:
                    if sy[0] in ['y']:
                        key = 'i' + sy[1]
                if sy[1] in ['u1', 'u2', 'u3', 'u4', 'un1', 'un2', 'un3', 'un4', 'uan1', 'uan2', 'uan3', 'uan4']:
                    if sy[0] in ['j', 'q', 'x', 'y']:
                        key = 'y' + sy[1]

                if key in results:
                    results[key].append(s)
                else:
                    results[key] = [s]
    keys = results.keys()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for key in sorted(keys):
            print(key, file=f)
            print(' '.join(results[key]), file=f)
            print(' ', file=f)
            print(key, results[key])
