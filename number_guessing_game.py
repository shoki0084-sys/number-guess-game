import random

def number_guessing_game():
    """
    1～100の間の数字を当てるゲーム
    """
    # 1～100の間のランダムな数字を生成
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("=" * 50)
    print("数字当てゲームへようこそ！")
    print("=" * 50)
    print(f"1～100の間の数字を当ててください。")
    print(f"最大{max_attempts}回まで挑戦できます。")
    print("-" * 50)
    
    while attempts < max_attempts:
        try:
            # 現在の試行回数と残り試行回数を表示
            remaining = max_attempts - attempts
            print(f"\n【試行回数: {attempts + 1}/{max_attempts}回目】")
            print(f"【残り試行回数: {remaining}回】")
            
            # ユーザーの入力を取得
            guess = int(input(f"予想する数字を入力してください: "))
            
            # 入力が1～100の範囲外の場合
            if guess < 1 or guess > 100:
                print("⚠️  1～100の間の数字を入力してください。")
                print("⚠️  この入力は試行回数にカウントされません。")
                print("-" * 50)
                continue
            
            attempts += 1
            
            print("-" * 50)
            print(f"あなたの予想: {guess}")
            
            # 数字が当たった場合
            if guess == secret_number:
                print("=" * 50)
                print(f"🎉 おめでとうございます！{attempts}回で当たりました！")
                print(f"答えは {secret_number} でした。")
                print("=" * 50)
                return
            
            # 数字が大きすぎる場合
            elif guess > secret_number:
                difference = guess - secret_number
                print("【ヒント】")
                if difference <= 5:
                    print("↓ 少し大きいです（答えに近い！）")
                    print("💡 もっと小さい数字を試してください")
                elif difference <= 10:
                    print("↓ 大きいです")
                    print("💡 もっと小さい数字を試してください")
                else:
                    print("↓ もっと小さいです")
                    print("💡 もっと小さい数字を試してください")
            
            # 数字が小さすぎる場合
            else:
                difference = secret_number - guess
                print("【ヒント】")
                if difference <= 5:
                    print("↑ 少し小さいです（答えに近い！）")
                    print("💡 もっと大きい数字を試してください")
                elif difference <= 10:
                    print("↑ 小さいです")
                    print("💡 もっと大きい数字を試してください")
                else:
                    print("↑ もっと大きいです")
                    print("💡 もっと大きい数字を試してください")
            
            # 試行回数の情報を再表示
            remaining = max_attempts - attempts
            print("-" * 50)
            print(f"📊 現在の試行回数: {attempts}回")
            if remaining > 0:
                print(f"📊 残り試行回数: {remaining}回")
            else:
                print("📊 これが最後の挑戦です！")
            print("-" * 50)
            
        except ValueError:
            print("⚠️  数字を入力してください。")
            print("⚠️  この入力は試行回数にカウントされません。")
            print("-" * 50)
    
    # 試行回数を使い切った場合
    print(f"💔 残念！{max_attempts}回の挑戦で当てられませんでした。")
    print(f"答えは {secret_number} でした。")
    print("=" * 50)

def play_again():
    """
    もう一度プレイするか確認
    """
    while True:
        choice = input("もう一度プレイしますか？ (y/n): ").lower()
        if choice == 'y' or choice == 'yes' or choice == 'はい':
            return True
        elif choice == 'n' or choice == 'no' or choice == 'いいえ':
            return False
        else:
            print("'y' または 'n' を入力してください。")

# メインループ
if __name__ == "__main__":
    while True:
        number_guessing_game()
        if not play_again():
            print("ゲームを終了します。ありがとうございました！")
            break



