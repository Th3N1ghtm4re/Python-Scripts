
# SecDel

**SecDel** is a simple Python script designed to securely delete files or directories by overwriting their contents multiple times before removal. This ensures that the data is unrecoverable by most file recovery tools. The script supports both files and directories and will recursively overwrite the contents of each file in a directory.

## Features

- Securely deletes files by overwriting with random data.
- Deletes files in directories, including subdirectories.
- Uses multiple overwrite passes (25 times) to make recovery difficult.
- Cleans up empty directories after file deletion.
- Prints success messages upon completion.

## Requirements

- Python 3.x
- No additional libraries or dependencies required.

## Usage

To securely delete a file or directory, run the script with the file or directory path as an argument:

```bash
python secdel.py {file_or_directory_path}
```

### Example

```bash
python secdel.py /path/to/file_or_directory
```

## How It Works

1. **File Deletion:** 
   - The file is overwritten 25 times with a mix of zeros (` `), random data, and ones (`Ăż`).
   - After multiple overwriting passes, the file is deleted using `os.remove()`.

2. **Directory Deletion:**
   - For directories, the script recursively traverses the directory and applies the file deletion process to each file.
   - Once all files are deleted, the empty directories are removed.

## Error Handling

- If the path is not a file or directory, the script will print an error message.
- If the number of arguments is incorrect, the script will show the correct usage.

## Example Output

```bash
Success
```

In case of an invalid file or directory path:

```bash
Error, not a file/directory
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE file](LICENSE) for more details.

---

Developed by [stigsec](https://github.com/stigsec).
