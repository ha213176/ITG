import webbrowser    
import googlemaps
import time


# gmaps=googlemaps.Client(key="這裡輸入你的API KEY")

urL='https://www.google.com/maps/dir/23.5601692,120.469598/台北101%2F世貿'
webbrowser.get('windows-default').open_new(urL)