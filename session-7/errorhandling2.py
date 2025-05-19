def process_numbers(data):
    results = []
    for item in data:
        try:
            number = float(item)
            results.append(number)
        except (ValueError, TypeError):
            print(f"Can't convert '{item}' to a float. Skipping...")
    return results


data = [10, "20", "not available", 30, "40.5", None, "0.1", "error"]
results = process_numbers(data)
print("Processed numbers:", results)
