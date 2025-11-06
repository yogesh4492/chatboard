def run_s3_ls(input_file):
    with open(input_file, "r") as f:
        paths = [line.strip().strip('"') for line in f if line.strip()]
    
    for i, path in enumerate(paths, start=1):
        output_file = f"{i}.txt"
        cmd = f'aws s3 sync "{path}" '
        with open("sync.txt",'a') as ap:
             ap.write(f"{cmd}\n")

if __name__ == "__main__":
    run_s3_ls("1.txt")