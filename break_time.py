import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program stated on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open("http://v.youku.com/v_show/id_XMTI4MTE1NTY0MA==.html")
    break_count = break_count + 1
