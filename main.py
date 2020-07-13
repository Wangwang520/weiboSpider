# -*- coding:utf-8 -*-
from weibo_fans import Weibo_fans
from weibo_follows import Weibo_follows
from weibo_profile import Weibo_profile
import threading

id ='2803301701'

fans = Weibo_fans(id)
follows = Weibo_follows(id)
profile_comments = Weibo_profile(id)

thred1 = threading.Thread(fans.run())
thred2 = threading.Thread(follows.run())
thred3 = threading.Thread(profile_comments.run())


thred1.start()
thred2.start()
thred3.start()


