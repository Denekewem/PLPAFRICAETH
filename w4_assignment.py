def file_read_write(input_file, output_file):
    try:
        with open(input_file, "r") as f:
            content = f.read()
            print("\n--- Original File Content ---")
            print(content)
        modified_content = content.upper()

        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"\nModified content written successfully to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write '{input_file}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = "modified_" + input_file  # Save as modified_<filename>

    file_read_write(input_file, output_file)


if __name__ == "__main__":
    main()
