import sys
import json
import yaml
import xmltodict

def main():
    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    input_ext = input_file.split('.')[-1]
    output_ext = output_file.split('.')[-1]

    data = None
    if input_ext == "json":
        with open(input_file, 'r') as f:
            data = json.load(f)
    elif input_ext in ["yml", "yaml"]:
        with open(input_file, 'r') as f:
            data = yaml.safe_load(f)
    elif input_ext == "xml":
        with open(input_file, 'r') as f:
            data = xmltodict.parse(f.read())
    else:
        print("Unsupported input format")
        return

    if output_ext == "json":
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
    elif output_ext in ["yml", "yaml"]:
        with open(output_file, 'w') as f:
            yaml.dump(data, f)
    elif output_ext == "xml":
        with open(output_file, 'w') as f:
            xml_str = xmltodict.unparse(data, pretty=True)
            f.write(xml_str)
    else:
        print("Unsupported output format")

if __name__ == "__main__":
    main()
