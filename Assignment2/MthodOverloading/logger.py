class Logger:
    def log(self, *args):
        if len(args) == 1:
            print(f"[INFO] {args[0]}")
        elif len(args) == 2:
            print(f"[{args[0].upper()}] {args[1]}")
        else:
            print("[UNKNOWN FORMAT]")

# Usage
log = Logger()
log.log("System started")
log.log("error", "File not found")
