def parse_links(file_path: str) -> list[str]:
    links: list[str] = []

    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read each line from the file
        for line in file:
            # Split the line by space character to separate words
            words: list[str] = line.split(" ")

            # Iterate through each word in the line
            for word in words:
                # Check if the word starts with 'http' to identify links
                if word.startswith("http"):
                    # Append the link to the list
                    links.append(word.strip())

    return links
