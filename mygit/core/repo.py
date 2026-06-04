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
        
        (self.mygit / "commits").mkdir(parents=True)
        (self.mygit / "snapshots").mkdir(parents=True)

        (self.mygit / "HEAD").write_text("")

        config = {
            "created_at": datetime.now().isoformat(),
            "version": "0.1"
        }

        (self.mygit / "config.json").write_text(json.dumps(config, indent=2))

        print(f"Repo initialisé")
