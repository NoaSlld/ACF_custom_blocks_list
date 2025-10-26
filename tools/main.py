import sys
from .upload_main import UploadMain

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else "upload"

    if command == "upload":
        UploadMain().run()
    else:
        print(f"❌ Commande inconnue : {command}")

if __name__ == "__main__":
    main()
