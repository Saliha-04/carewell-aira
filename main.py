from aira.chat_session import run_chat


def main():
    try:
        run_chat()
    except KeyboardInterrupt:
        print("\nAira: Goodbye! Take care.")


if __name__ == "__main__":
    main()