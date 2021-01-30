import speedtest

test = speedtest.Speedtest()

#check donload speed
download = test.download()

#check upload speed
upload = test.upload()

#print the results by converting to GB and rounding
print(f'Download speed: {round(download/1024**2,2)} GB')
print(f'Upload speed: {round(upload/1024**2,2)} GB')
