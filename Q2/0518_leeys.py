function_list = list(map(int, input().split()))
speeds = list(map(int, input().split()))

c = [function_list[i] + speeds[i] for i in range(len(int(function_list)))]
print(c)