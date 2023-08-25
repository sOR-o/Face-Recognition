import os

def rename(path):
    if not os.path.exists(path):
        print("Folder does not exist.")
        return
    
    extensions = ['.jpg', '.jpeg', '.png']  # Add more extensions if needed
    images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1].lower() in extensions]
    
    if not images:
        print("No image files found in the folder.")
        return
    
    count = 1
    for oldName in images:
        extension = os.path.splitext(oldName)[1]
        newName = f"{count}{extension}"
        oldPath = os.path.join(path, oldName)
        newPath = os.path.join(path, newName)
        
        os.rename(oldPath, newPath)
        print(f"Renamed {oldName} to {newName}")
        
        count += 1

if __name__ == "__main__":
    path = input("Enter the folder path: ")
    rename(path)