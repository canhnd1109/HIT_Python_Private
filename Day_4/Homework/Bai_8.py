
player1_wins = []
player2_wins = []
round_number = 1

while True:
    print("Round", round_number)
    n = int(input("Nhập n (số nguyên dương): "))
    k = int(input("Nhập k (số nguyên dương < n): "))

    while n <= k:
        print("Lỗi: n phải lớn hơn k. Vui lòng nhập lại.")
        n = int(input("Nhập n (số nguyên dương): "))
        k = int(input("Nhập k (số nguyên dương < n): "))

    current_player = 1
    while True:
        print("Lượt của người chơi", current_player)
        move = int(input("Nhập một số từ 1 đến " + str(min(n, k)) + ": "))

        while move < 1 or move > min(n, k):
            print("Lỗi: Số không hợp lệ. Vui lòng nhập lại.")
            move = int(input("Nhập một số từ 1 đến " + str(min(n, k)) + ": "))

        n -= move

        if n <= 0:
            print("Người chơi", current_player, "thắng round", round_number)
            if current_player == 1:
                player1_wins.append(round_number)
            else:
                player2_wins.append(round_number)
            break

        current_player = 2 if current_player == 1 else 1

    choice = input("Bạn có muốn tiếp tục không? (YES/NO): ")
    while choice.upper() != "YES" and choice.upper() != "NO":
        print("Lỗi: Phải chọn YES hoặc NO. Vui lòng nhập lại.")
        choice = input("Bạn có muốn tiếp tục không? (YES/NO): ")

    if choice.upper() == "NO":
        break

    round_number += 1

print("\nThống kê game:")
total_rounds = round_number - 1
print("Tổng số round:", total_rounds)

player1_total_wins = len(player1_wins)
player2_total_wins = len(player2_wins)
print("Người chơi 1 thắng", player1_total_wins, "rounds")
print("Người chơi 2 thắng", player2_total_wins, "rounds")

if player1_total_wins > player2_total_wins:
    print("Người chơi 1 thắng chung cuộc")
    print("Các round mà người chơi 1 đã thắng:", player1_wins)
elif player2_total_wins > player1_total_wins:
    print("Người chơi 2 thắng chung cuộc")
    print("Các round mà người chơi 2 đã thắng:", player2_wins)
else:
    print("Hai người chơi hoà")

