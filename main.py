from shipment_processor import ShipmentProcessor

def main():
    processor = ShipmentProcessor()
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            result = processor.process_line(line)
            outfile.write(result + "\n")
            print(result)

if __name__ == "__main__":
    main()
