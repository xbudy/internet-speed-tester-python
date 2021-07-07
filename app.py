import speedtest

tester=speedtest.Speedtest()


print('Searching for the best server ..')
bestServer=tester.get_best_server()
print(f'Selecting {bestServer["host"]} located in {bestServer["country"]},{bestServer["name"]}')

print('Checking download speed ..')
downloadSpeed=tester.download()
print('Done !')

print('Checking upload speed ..')
uploadSpeed=tester.upload()
print('Done !')

ping=tester.results.ping

print('Results :')
print(f'-Download speed : {downloadSpeed/1048576 :.2f} Mbits/s')
print(f'-Upload speed : {uploadSpeed/1048576 :.2f} Mbits/s')
print(f'-Ping : {ping :.2f} ms')
