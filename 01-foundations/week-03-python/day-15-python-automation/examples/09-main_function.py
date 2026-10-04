def check_server():
    print("Checking server...")


def main():
    print("Starting server health check")

    check_server()

    print("Health check completed")


if __name__ == "__main__":
    main()

Understand this carefully.

if __name__ == "__main__":
    main()

means the main() function executes when this file is run directly.