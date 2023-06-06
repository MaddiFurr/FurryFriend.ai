import speedtest

print(f"Best Server {speedtest.Speedtest().get_best_server()}")
tester = speedtest.Speedtest()
tester.get_best_server()
print(f"Your ping is: {tester.results.ping} ms")
print(f"Your download speed: {round(tester.download() / 1000 / 1000, 1)} Mbit/s")
print(f"Your upload speed: {round(tester.upload() / 1000 / 1000, 1)} Mbit/s")
print("speedtest end")