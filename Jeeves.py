from app.application import manager
from app.command.command import *
from app.lib.www import *

# コマンドのマッピング
manager.add_command("runserver", server)
manager.add_command("runbatch", batch)
manager.add_command("learning", learning)
manager.add_command("show", show)
manager.add_command("init", init)

if __name__ == "__main__":
    try:
        import sys
        sys.exit(manager.run())
    except Exception as e:
        import traceback
        traceback.print_exc()
