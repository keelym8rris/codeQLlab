import time
import sys

def loading_animation():
    print("Loading something awesome...")
    print()
    
    # Progress bar animation
    bar_length = 40
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        filled = '█' * i
        empty = '░' * (bar_length - i)
        sys.stdout.write(f'\r[{filled}{empty}] {percent:.0f}%')
        sys.stdout.flush()
        time.sleep(0.05)
    
    print("\n")
    print(" Done! ")
    print()
    
    # Spinning animation
    print("Thinking", end="")
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for _ in range(20):
        for symbol in spinner:
            sys.stdout.write(f'\rThinking {symbol}')
            sys.stdout.flush()
            time.sleep(0.1)
    
    print("\r✓ Complete!     ")
    print()
    print("🎉 Have a great day! 🎉")

if __name__ == "__main__":
    loading_animation()
