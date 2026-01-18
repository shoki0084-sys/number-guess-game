import random

if __name__ == "__main__":
    # 1～100の間のランダムな数字を生成
    secret_number = random.randint(1, 100)
    MAX_ATTEMPTS = 7
    attempts = MAX_ATTEMPTS
    
    print("=" * 50)
    print("数当てゲームへようこそ！")
    print("1～100の間の数字を当ててください。")
    print(f"最大{MAX_ATTEMPTS}回まで挑戦できます。")
    print("=" * 50)
    
    while attempts > 0:
        try:
            guess = int(input(f"\n数字を入力してください（1〜100）: "))
            
            # 入力値の範囲チェック
            if guess < 1 or guess > 100:
                print("⚠️  1～100の間の数字を入力してください。")
                continue
            
            attempts -= 1
            
            if guess == secret_number:
                print("\n" + "=" * 50)
                print("🎉 正解！")
                print(f"答えは {secret_number} でした。")
                print(f"試行回数: {MAX_ATTEMPTS - attempts} 回")
                print("=" * 50)
                break
            elif guess < secret_number:
                print(f"📈 もっと大きい！ 残り{attempts}回")
            else:
                print(f"📉 もっと小さい！ 残り{attempts}回")
                
        except ValueError:
            print("⚠️  数字を入力してください。")
        except KeyboardInterrupt:
            print("\n\nゲームを終了します。")
            break
        except Exception as e:
            print(f"⚠️  エラーが発生しました: {e}")
    else:
        print("\n" + "=" * 50)
        print("💀 ゲームオーバー")
        print(f"正解は {secret_number} でした")
        print("=" * 50)


