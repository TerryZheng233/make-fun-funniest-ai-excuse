import os

EXCUSE = "Sorry, I finished the wrong task so efficiently that I had already thanked myself for the feedback and closed the ticket before anyone noticed."

def main():
    out_dir = "/output" if os.path.isdir("/output") or os.access("/", os.W_OK) else "output"
    # In the grading sandbox the program writes to /output/entry.txt
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    except Exception:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(EXCUSE)

if __name__ == "__main__":
    main()
