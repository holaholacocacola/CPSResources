import os
import shutil

# CURR_PATH = os.path.abspath(os.path.dirname(__file__))
ARCHIVES_MAP = {
    "../dist/legends/CPSLegendsIconPack": "../dist/legends/Data",
    "../dist/vanilla/CPSVanillaIconPack": "../dist/vanilla/Data",
    "../dist/game-icons/CPSGameIconsPack": "../dist/game-icons/Data"
    }

def main():

    for archive, archive_path in ARCHIVES_MAP.items():
        try:
            shutil.make_archive(archive, 'zip', archive_path)
            print (f"Generated {archive}")
        except Exception as e:
            print (f"Error making archives: {e}")
    
    
if __name__ == "__main__":
    main();
