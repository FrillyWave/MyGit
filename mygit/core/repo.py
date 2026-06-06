from pathlib import Path
import json
from datetime import datetime

class Repo: 
    def __init__(self, root="."):
        self.root = Path(root)
        self.mygit = self.root / ".mygit"

    def init(self):
        if self.mygit.exists():
            print("Repo déjà initialisé")
            return
        
        self.mygit.mkdir()

        for dirname in ["commits", "objects"]:
            (self.mygit / dirname).mkdir()

        head = {
            "commit": None
        }

        index = {}

        config = {
            "created_at": datetime.now().isoformat(),
            "version": "0.1"
        }

        (self.mygit / "HEAD").write_text(json.dumps(head, indent=2))

        (self.mygit / "index.json").write_text(json.dumps(index, indent=2))

        (self.mygit / "config.json").write_text(json.dumps(config, indent=2))

        print(f"Repo initialisé")
