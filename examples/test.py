import time

import never_jscore


ctx = never_jscore.Context(enable_logging=False)  # Disable logging to avoid massive timer output
with open('备份.js',encoding='utf-8')as f:
    data = f.read()

# with open('sbsd_js.js',encoding='utf-8')as f:
#     js = f.read()

ctx.compile(data)

ck = f'bm_lso=8ECC43BEDB305EFD577ACC3F1E91AC5262FD019FB784B74ED2CEBAA0702C613A~YAAQzbkhF2BoATWaAQAAqmB4fAW9w7CwHBRWYRSnl6GgEK177cLecAg4VgrpWedEP5CbF1t/xmGdkyazeeK37BF3eGaEU8M7ju6t/iIkHMtbpnZ2REoIPaxGkxxMVwJNAuk0Jz/GdAl8jb6CcPX+1X6gL1nlklH+FgZ2Hho75mqr+Q6O7zcC/M/52j98A2KdwrvC8SCkLwS/A3mbHE23vi2C/ypjR2JoOSchLwgD4HPIssA+d4lR+AUMqxnY3OIS9EesI2uEre//FkcbwNJW2rQNishZAyfPAuD6zEWYcTWy/CGICc03tmsl+AEh9pfakHch23HHqCICT91fItb/uxeCaz9vj9Jf8qX+ou4tdp8OoeNuyzPe80/lCdqa7hzgu1oBC/Xo4LcPqDQCwwKTBOxOz04Cg/zhgXNs0V4+ivCd02nTE6bB4QopPOt4ryfNPWHw4yec6icqKRKpD7Q=^{str(int(time.time() * 1000))}; _abck=16CB6A5F1B978C9571A4EC18C8B2FD1E~-1~YAAQzbkhF4xtATWaAQAABoB4fA7Juvn5XP3zFKH1KM/0yp5osGZeRiV/OfF6u5W8LOhr9y8mD1Qx6C50EqkXzeMxECo1WDSbgYt1YsnVqKhj4JQQzDr+KIDtuP5yCmZ7i8aB5i6PXtIqAZf4uRbNN4ICuGozWqdjSS22RgaOXG3eyRb/Qrb/zWmRjKW4OKqK05Y7Zy7edgQDJ+ikmQ4ldCNZ0NwZQWtyTDQA/NkdKtsuEeHWDpdHsIo/LaPAfnijxF5qTaPOzPcUZMVXI/D4LcQcSW1C5euKWMk4kaF/H93SKm1Gh3FkWwRFrt3i8kZfnrzf3/duDhPCgxBEJFqgCHV884Y6RRrxnW/JhU3S847OxkQNl26wos6ShMFn0wfLy3W1yc22ptOL7ud+C601LDHfoV6fs6H93vI01MCCsF8IWxVfAzM5ThUIrfLzdXHWPW7Op0kTm9eDQQ9LEJ/3SpmpUmCIRGkwMxDHpUrL3R0SwZaKwyW7DhND340S3FkJyos0ACcP40BLelzTrHc3KTrSx1czn5he6M4Hl3vTdMrL24KCBcsSq9srcnizWc0pRxhS/yNCpc8DBLeYno58Akg10bHhLv/XcBN2ywH4O7v6sUtB+UJO38u37S2SXiOUnx0ZWab+nZAhyHpTv9wMxI5Zcel3ymSC7P2gPrq8TXci8TytxA/rp+E7nWQyTm4CcUvpwI1hLqJFTl0/uMKIwHy3VQXNXj5sHba7zy2gQT8PKaLsZtHLI79lvBrixxAVfgltuHHiICIpMzKo3u755gslONMvZyGJlngkvt7Jpj4ky0P0ybZaF6JhnFgO63iJnlNtxwIfDrtpVLGBSExVU1a9QHiP9/q5va2fS9nqUjU9rYmyS9dAXsJDeb/hr81Zeu75rN0iMfWTc5N4E+BEVcrmtnLMeD/C1V71j91Biq8upK4QUMGkjvUuznb3OwXxoFuqe6g86vdzrZcp2cknb2QXUHdpySYyIB5uYdz5cDpT~-1~-1~-1~AAQAAAAE%2f%2f%2f%2f%2f2FHLTUTN+obhFnAKqaA5cJvNw9lbEnVKf31d%2f2xmw2mTcGSyMJWjAmXu6n++2fE6w8iFxpZ8kPcmIP0Qwxz1+hsh2pSb21NmgSbRjOpeFBh3+v%2f5ZohUheZfXb7a6J7aXy+0ql3pAPhlqjyoFTBBbOgH1zyglNJm2XwZ2kvVw%3d%3d~1763024923'
# print(ck)

print(ctx.call('get_sbsd_body', [ck,'']))
# print(ctx.evaluate(data))



# ctx2 = py_mini_racer.MiniRacer()
# ctx2.eval(data)

