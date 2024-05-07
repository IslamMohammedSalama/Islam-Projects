from speedtest import Speedtest

print('Getting Speed...')
st = Speedtest()
print('Getting Download Speed...') 
download_speed = st.download()
print('Getting Upload Speed...')
upload_speed = st.upload()
print('Getting Ping Load...')
ping  = st.results.ping()

print(f"Download speed: {download_speed / 1024 / 1024:.5f} Mbps .")
print(f"Upload speed: {upload_speed / 1024 / 1024:.5f} Mbps .")
print(f"Ping Load: {ping :.f2} Ping .")