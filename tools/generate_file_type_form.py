import warnings

from transfer.mapping import file_extension2file_type, file_type2lexer

if __name__ == "__main__":
    file_type2lexer_and_extension = {}

    # get mapping
    for file_type, lexer in file_type2lexer.items():
        file_type2lexer_and_extension[file_type] = {"lexer": lexer, "extension": []}

    for extension, file_type in file_extension2file_type.items():
        if file_type in file_type2lexer_and_extension:
            file_type2lexer_and_extension[file_type]["extension"].append(extension)
        else:
            warnings.warn("Unknown file type: {}".format(file_type))

    # generate markdown file
    with open("FILE_TYPE_MAPPING.md", "w+") as f:
        f.writelines("## File Type Mapping\n\n")
        f.writelines("| Type | Extension | Lexer |\n")
        f.writelines("| :--: | :-------: | :---: |\n")

        for file_type, lexer_and_extension in file_type2lexer_and_extension.items():
            lexer = lexer_and_extension["lexer"]
            extensions = ", ".join(lexer_and_extension["extension"])
            f.writelines(f"| {file_type} | {extensions} | {lexer} |\n")
