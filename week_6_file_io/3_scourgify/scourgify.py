import sys, csv

def main():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Not enough arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"{sys.argv[1]} is not a CSV file")
    else:
        scourgify(sys.argv[1], sys.argv[2])

def scourgify(input_file, output_file):
    try:
        students = []
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name = row["name"].split(", ")
                students.append({"first": first_name, "last": last_name, "house": row["house"]})
        with open(output_file, "w") as file2:
            writer = csv.DictWriter(file2, ["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not find {input_file}")

if __name__ == "__main__":
    main()
